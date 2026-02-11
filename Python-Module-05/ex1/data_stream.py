#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_stream.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/10 09:02:22 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/11 15:05:14 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    """
    This class is an abstract class that represents a Stream. A stream can
    process a batch of data or filter a batch of data.
    """
    def __init__(self, stream_id: str, stream_type: str,
                 batch_type: str) -> None:
        """
        This function initializes the DataStream with it's
        following attributes.

        Args:
            stream_id (str): The ID of the streaM.
            stream_type (str): The Type of the stream (Environmental,
            Financial, System Events).
            batch_type (str): The type of the batch (sensor, transaction,
            event)
        """
        self.stats: dict[str, Union[str, int, float]] = {}
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.batch_type: str = batch_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        This function processes the batch by applying
        operation on it. Each Stream type has it's own way
        to process data.

        Args:
            data_batch (List[Any]): The data to be processed.

        Returns:
            str: The process of the batch.
        """
        ...

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        This function filters data based on a specific criteria.
        The criteria is optional.

        Args:
            data_batch (List[Any]): The data to be filtered.
            criteria (Optional[str], optional): The criteria
            to base the filtering. Defaults to None.

        Returns:
            List[Any]: The filtered data batch .
        """
        if not isinstance(data_batch, list):
            return []
        if criteria is None:
            return data_batch
        else:
            return [data for data in data_batch if criteria in str(data)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        This function returns the dictionary containting the
        statistics of the stream.

        Returns:
            Dict[str, Union[str, int, float]]: The statistics
            of the stream.
        """
        return self.stats


class SensorStream(DataStream):
    """
    This class represents a special type of stream. A Sensor Stream.
    A Sensor stream accepts data in a dictionary, it's main use is
    mesuring.
    """
    def __init__(self, stream_id: str) -> None:
        """
        This function initializes the stream with a stream ID.

        Args:
            stream_id (str): The ID of the stream.
        """
        print("Initializing Sensor Stream...")
        super().__init__(stream_id, "Environmental Data", "sensor batch")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        This function processes a data batch by parsing the
        given dictionary and calculating the average temperature.

        Args:
            data_batch (List[Any]): The data to be processed.

        Returns:
            str: The number of data processed and the average temperature.
        """
        try:
            temperatures = 0
            for data in data_batch:
                informations = data.split(":")
                self.stats[informations[0]] = 0

            for data in data_batch:
                informations = data.split(":")
                if informations[0] == "temp":
                    temperatures += 1
                self.stats[informations[0]] += float(informations[1])

            if temperatures > 0:
                avg = self.stats['temp'] / temperatures
            else:
                avg = 0

            return f"Sensor analysis: {len(data_batch)} readings processed, \
avg temp: {avg}"
        except ValueError:
            return "Please pass a valid sensor batch. A valid sensor \
batch is of the form ['temp:22.5', 'humidity:65', 'pressure:1013']"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        This function filters data based on a specific criteria.
        The criteria is optional.

        Args:
            data_batch (List[Any]): The data to be filtered.
            criteria (Optional[str], optional): The criteria
            to base the filtering. Defaults to None.

        Returns:
            List[Any]: The filtered data batch .
        """
        filtered_data: List[Any] = []
        for data in data_batch:
            if ":" in str(data):
                informations: List[str] = data.split(":")
                if informations[0] == criteria:
                    filtered_data.append(data)
        return filtered_data


class TransactionStream(DataStream):
    """
    This class represents a special type of stream. A Transaction Stream.
    A Transaction stream accepts data in a list, it's main use is
    calculating the net flow.
    """
    def __init__(self, stream_id: str) -> None:
        """
        This function initializes the stream with a stream ID.

        Args:
            stream_id (str): The ID of the stream.
        """
        print("Initializing Transaction Stream...")
        super().__init__(stream_id, "Financial Data", "transaction batch")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        This function processes a data batch by parsing the
        given list of actions and calculating the net flow.

        Args:
            data_batch (List[Any]): The data to be processed.

        Returns:
            str: The number of data processed and the average temperature.
        """
        self.stats["transactions"] = len(data_batch)
        self.stats["flow"] = 0
        try:
            for data in data_batch:
                informations: List[str] = data.split(":")
                if informations[0] == "buy":
                    self.stats["flow"] += int(informations[1])
                elif informations[0] == "sell":
                    self.stats["flow"] -= int(informations[1])
            if self.stats["flow"] < 0:
                self.stats["flow"] = f"-{self.stats['flow']}"
            elif self.stats["flow"] > 0:
                self.stats["flow"] = f"+{self.stats['flow']}"
            return f'Transaction analysis: {self.stats["transactions"]} \
operations, net flow: {self.stats["flow"]} units'
        except Exception:
            return "Data batch not valid, please provide a batch of the \
form ['buy:n', 'sell:n', ...]"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        This function filters data based on a specific criteria.
        The criteria is optional.

        Args:
            data_batch (List[Any]): The data to be filtered.
            criteria (Optional[str], optional): The criteria
            to base the filtering. Defaults to None.

        Returns:
            List[Any]: The filtered data batch .
        """
        filtered_data: List[Any] = []
        for data in data_batch:
            if ":" in str(data):
                informations: List[str] = data.split(":")
                if informations[0] == criteria:
                    filtered_data.append(data)
        return filtered_data


class EventStream(DataStream):
    """
    This class represents a special type of stream. An Event Stream.
    An Event stream accepts data in a list, it's main use is
    calculating the actions of a user.
    """
    def __init__(self, stream_id: str) -> None:
        """
        This function initializes the stream with a stream ID.

        Args:
            stream_id (str): The ID of the stream.
        """
        print("Initializing Event Stream...")
        super().__init__(stream_id, "System Events", "event batch")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        This function processes a data batch by parsing the
        given list of actions and computing the actions of
        a user.

        Args:
            data_batch (List[Any]): The data to be processed.

        Returns:
            str: The number of data processed and the average temperature.
        """
        self.stats["events"] = len(data_batch)
        self.stats["errors"] = 0
        for data in data_batch:
            if data == "error":
                self.stats["errors"] += 1
        if self.stats["errors"] == 1:
            return f"Event analysis: {self.stats['events']} events, \
{self.stats['errors']} error detected"
        else:
            return f"Event analysis: {self.stats['events']} events, \
{self.stats['errors']} errors detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        This function filters data based on a specific criteria.
        The criteria is optional.

        Args:
            data_batch (List[Any]): The data to be filtered.
            criteria (Optional[str], optional): The criteria
            to base the filtering. Defaults to None.

        Returns:
            List[Any]: The filtered data batch .
        """
        filtered_data: List[Any] = []
        for data in data_batch:
            if data == criteria:
                filtered_data.append(data)
        return filtered_data


class StreamProcessor:
    """
    This processor is able to manage multiple streams of multiple types.
    """
    def __init__(self) -> None:
        """
        This function initializes the stream processor with
        an empty dictionary of streams.
        """
        self.streams: Dict[str, DataStream] = {}

    def add_stream(self, stream: DataStream):
        """
        This function adds a stream to the streams
        dictionary.

        Args:
            stream (DataStream): The stream to add.
        """
        if isinstance(stream, DataStream):
            self.streams[stream.stream_id] = stream
        else:
            print("Error: Invalid stream type")

    def process_streams(self, batches: Dict[str, Any]) -> None:
        """
        This function processes all of the streams present in
        the dictionary.

        Args:
            batches (Dict[str, Any]): The different datas for
            each stream.
        """
        print("Batch 1 Results:")
        try:
            for stream in self.streams.keys():
                if stream in batches:
                    print(f"- \
{self.streams[stream].process_batch(batches[stream])}")
        except Exception:
            print("Error occured while processing the streams.")

    def filter_streams(self, bat: Dict[str, Any],
                       crit: Dict[str, Any]) -> None:
        """
        This function filters all of the streams present in
        the dictionary.

        Args:
            bat (Dict[str, Any]): The different datas for
            each stream.
            crit (Dict[str, Any]): The different criterias for
            each data batch.
        """
        print("\nStream filtering active: High-priority data only")
        filtered_results = []
        for s in self.streams.keys():
            if s in bat and s in crit:
                result = self.streams[s].filter_data(bat[s], crit[s])

                if len(result) > 0:
                    count = len(result)
                    st_type = self.streams[s].stream_type

                    if "Environmental" in st_type:
                        filtered_results.append(f"{count} critical sensor \
alerts")
                    elif "Financial" in st_type:
                        filtered_results.append(f"{count} large transaction")
                    elif "System" in st_type:
                        filtered_results.append(f"{count} critical events")

        print(f"Filtered results: {', '.join(filtered_results)}")


def main() -> None:
    """
    Main function that initializes objects and
    runs the required tests.
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    ss = SensorStream("SENSOR_001")
    sensors = ['temp:22.5', 'humidity:65', 'pressure:1013']
    print(f"Processing sensor batch: {sensors}")
    print(ss.process_batch(sensors))
    print("")

    ts = TransactionStream("TRANS_001")
    transactions = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transactions}")
    print(ts.process_batch(transactions))
    print("")

    es = EventStream("EVENT_001")
    events = ["login", "error", "logout"]
    print(f"Processing event batch: {events}")
    print(es.process_batch(events))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    data_batch = {ss.stream_id: sensors,
                  ts.stream_id: transactions,
                  es.stream_id: events}
    filters = {ss.stream_id: "temp",
               ts.stream_id: "buy",
               es.stream_id: "error"}
    sp = StreamProcessor()
    sp.add_stream(ss)
    sp.add_stream(ts)
    sp.add_stream(es)
    sp.process_streams(data_batch)
    sp.filter_streams(data_batch, filters)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
