#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 09:01:40 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/20 15:02:43 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import importlib.util
import importlib.metadata


def packages_present() -> dict[str, bool | list]:
    """
    This functions checks whether the current environment
    has all of the required packages installed.

    Returns:
        dict[str, bool | list]: A dictionary containing each package
        and if they are installed or not along with their corresponding
        message.
    """
    packages_status = {
        "installed": True,
        "numpy": [False, "Calculations ready"],
        "pandas": [False, "Data manipulation ready"],
        "requests": [False, "Network access ready"],
        "matplotlib": [False, "Visualization ready"]
    }
    for package in list(packages_status.keys())[1:]:
        if importlib.util.find_spec(package) is not None:
            packages_status[package][0] = True
        else:
            packages_status["installed"] = False
    return packages_status


def calculate_and_plot() -> None:
    """
    This funtion generates a data pattern of random numbers
    and plots a graph of the different values.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.DataFrame({
        "a": np.arange(1000),
        "c": np.random.randint(0, 50, 1000),
        "d": np.random.randn(1000)
    })
    df["b"] = df["a"] + 20 * np.random.randn(1000)
    plt.scatter("a", "b", c="c", s=df["d"].abs() * 2, data=df)
    plt.xlabel("Data A")
    plt.ylabel("Data B")
    plt.savefig("matrix_analysis.png")


def main() -> None:
    """
    This function tests and runs the main program.
    """
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    package_check = packages_present()
    if not package_check["installed"]:
        for package in list(package_check.keys())[1:]:
            status = "OK" if package_check[package][0] else "KO"
            if status == "OK":
                version = importlib.metadata.version(f"{package}")
                message = package_check[package][1]
                print(f"[{status}] {package} ({version}) - {message}")
            else:
                print(f"[{status}] {package} - Missing")
        print("\nPlease make sure to install all of the required packages.\n")
        print("""INSTALL GUIDE:
Installing with pip:
$> pip install -r requirements.txt
$ python3 loading.py

Installing with Poetry:
$> poetry install
$ poetry run python loading.py""")
    else:
        for package in list(package_check.keys())[1:]:
            version = importlib.metadata.version(f"{package}")
            message = package_check[package][1]
            print(f"[OK] {package} ({version}) - {message}")
        try:
            calculate_and_plot()
            print("""\nAnalyzing Matrix data...
Processing 1000 data points...
Generating visualization...

Analysis complete!
Results saved to: matrix_analysis.png""")
        except Exception as e:
            print(f"Error occured while plotting: {e}")


if __name__ == "__main__":
    main()
