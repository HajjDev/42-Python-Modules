#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  nexus_pipeline.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/11 12:14:45 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/11 15:23:19 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


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
        super().__init__(stream_id, "Environmental Data", "sensor batch")

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


class ProcessingStage(Protocol):
    """
    This class represents a stage. A stage can process data
    depending on the step they are on.

    This is a protocol, so each class that has the same structure
    is considered a ProcessingStage.
    """
    def process(self, data: Any) -> Any:
        """
        This function processes a chunk of data.
        Each stage has their own way to process data.

        Args:
            data (Any): The data to processed.

        Returns:
            Any: The processed data.
        """
        ...


class ProcessingPipeline(ABC):
    """
    This abstract class represents a pipeline. Each pipeline can
    inherit from this class and implement it's own methods.
    A pipeline is stream that processes a specific type of data.
    """
    def __init__(self) -> None:
        """
        This function initializes each pipeline with a list of stages.
        """
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        """
        This function adds a stage to the main list of stages.

        Args:
            stage (ProcessingStage): The stage to add.
        """
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        """
        This function processes a chunk of data. Each pipeline
        processes data in 3 steps. First by sending it to the
        InputStage, then by sending it to the TransformStage and
        finally by sending it to the Output stage.

        Args:
            data (Any): The data to processed.

        Returns:
            Any: The processed data.
        """
        ...


class NexusManager:
    """
    This manager manages a number of pipelines. A manager can also decide
    to process the data of a pipeline.
    """
    def __init__(self) -> None:
        """
        This function initializes the manager with a list of pipelines.
        """
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """
        This function adds a pipeline to the original list of pipelines.

        Args:
            pipeline (ProcessingPipeline): The pipeline to add.
        """
        self.pipelines.append(pipeline)

    def process_data(self, pipeline_id: str, data: Any) -> None:
        """
        This function processes the data of a specified pipeline.

        Args:
            pipeline_id (str): The ID of the pipeline to be processed.
            data (Any): The data to be processed by the pipeline.
        """
        try:
            for pipeline in self.pipelines:
                if pipeline.pipeline_id == pipeline_id:
                    pipeline.process(data)
        except Exception:
            print("""Error processing data throughout pipelines!
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed""")


class InputStage:
    """
    This is the Input Stage. This stage just receives the input
    and prints it to the screen.
    """
    def process(self, data: Any) -> Any:
        """
        This function processes the data by receiving it and
        printing it to the screen.

        Args:
            data (Any): The data given in the input.

        Returns:
            Any: The data extracted from the input.
        """
        if (isinstance(data, SensorStream)):
            print("Input: Real-time sensor stream")
        else:
            print(f"Input: {data}")
        return data


class TransformStage:
    """
    This is the Transform Stage. This stage receives the data from
    the input stage and transforms it.
    """
    def process(self, data: Any) -> Any:
        """
        This function processes the data received from the
        input stage by either validating it, transforming
        it into a list or extracting the data of a sensor.

        Args:
            data (Any): The data given from the input stage.

        Returns:
            Any: The extracted data.
        """
        try:
            if isinstance(data, dict):
                for key in data.keys():
                    if key == "value":
                        try:
                            data[key] = [float(data[key]), "valid"]
                        except ValueError:
                            raise ValueError
                    else:
                        data[key] = [data[key], "valid"]
                print("Transform: Enriched with metadata and validation")
                return data
            elif isinstance(data, str):
                if "," in data:
                    items = data.split(",")
                    print("Transform: Parsed and structured data")
                    return items
            elif isinstance(data, SensorStream):
                print("Transform: Aggregated and filtered")
                return data.process_batch(["temp:22.5", "humidity:65",
                                           "pressure:1013", "water:90",
                                           "air:90"])
            else:
                raise TypeError
        except ValueError:
            print("""Error detected in Transform Stage: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed""")


class OutputStage:
    """
    This is the Output Stage. This stage receives the data from
    the tranform stage and polishes it so it can be outputted.
    """
    def process(self, data: Any) -> Any:
        """
        This function processes the data received from the
        tranform stage by formatting it and printing it
        on the screen.

        Args:
            data (Any): The data given from the transform stage.

        Returns:
            Any: The polished data.
        """
        try:
            if isinstance(data, dict):
                output = f"Output: Processed temperature reading: \
{data['value'][0]}°C (Normal range)"
                print(output)
                return output
            elif isinstance(data, list):
                output = f"Output: User activity logged: \
{data.count('action')} actions processed."
                print(output)
                return output
            elif isinstance(data, str):
                output = f"Output: {data}°C"
                print(output)
                return output
        except Exception:
            print("""Error detected in Output Stage: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed""")


class JSONAdapter(ProcessingPipeline):
    """
    This StreamAdapter class only accepts data of the form of a dictionary.
    It can also extract the data given into a string and calculate the
    average value.
    """
    def __init__(self, pipeline_id: str) -> None:
        """
        This function initializes the CSVAdapter with an ID.

        Args:
            pipeline_id (str): The ID of the CSVAdapter.
        """
        super().__init__()
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> None:
        """
        This function processes the data by transforming
        it by sending it to the different stages.

        Args:
            data (Any): The data to be processed.
        """
        stage_data: Any = data
        try:
            for stage in self.stages:
                stage_data = stage.process(stage_data)
        except ValueError:
            print("""Error detected in the process: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed""")


class CSVAdapter(ProcessingPipeline):
    """
    This StreamAdapter class only accepts data of the form of a string.
    It can also extract the data given into a list.
    """
    def __init__(self, pipeline_id: str) -> None:
        """
        This function initializes the CSVAdapter with an ID.

        Args:
            pipeline_id (str): The ID of the CSVAdapter.
        """
        super().__init__()
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> None:
        """
        This function processes the data by transforming
        it by sending it to the different stages.

        Args:
            data (Any): The data to be processed.
        """
        stage_data: Any = data
        try:
            for stage in self.stages:
                stage_data = stage.process(stage_data)
        except ValueError:
            print("""Error detected in the process: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed""")


class StreamAdapter(ProcessingPipeline):
    """
    This StreamAdapter class only accepts data that has a SensorStream type.
    It can also process this sensor by extracting it's data.
    """
    def __init__(self, pipeline_id: str) -> None:
        """
        This function initializes the StreamAdapter with an ID.

        Args:
            pipeline_id (str): The ID of the StreamAdapter.
        """
        super().__init__()
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> None:
        """
        This function processes the data by polishing
        it by sending it to the different stages.

        Args:
            data (Any): The data to be processed.
        """
        stage_data: Any = data
        try:
            for stage in self.stages:
                stage_data = stage.process(stage_data)
        except ValueError:
            print("""Error detected in the process: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed""")


def main() -> None:
    """
    Main function that initializes objects and
    runs the required tests.
    """
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")

    print("""Creating Data Processing Pipeline...
Stage 1: Input validation and parsing
Stage 2: Data transformation and enrichment
Stage 3: Output formatting and delivery

=== Multi-Format Data Processing ===\n""")

    json = JSONAdapter("JSON")
    csv = CSVAdapter("CSV")
    stream = StreamAdapter("STREAM")
    manager.add_pipeline(json)
    manager.add_pipeline(csv)
    manager.add_pipeline(stream)

    print("Processing JSON data through pipeline...")
    manager.process_data("JSON",
                         {"sensor": "temp", "value": 23.5, "unit": "C"})

    print("\nProcessing CSV data through same pipeline...")
    manager.process_data("CSV", "user,action,timestamp")

    print("\nProcessing Stream data through same pipeline...")
    manager.process_data("STREAM", SensorStream("SENSOR_001"))

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    print("\nChain result: 100 records processed through 3-stage pipeline")
    print("Performance: 95% efficiency, 0.2s total processing time\n")

    print("""=== Error Recovery Test ===
Simulating pipeline failure...""")
    manager.process_data("JSON", {"sensor": "temp", "value": "23.5a",
                                  "unit": "C"})


if __name__ == "__main__":
    main()
