import pandas as pd
from typing import List

class PerfDataProcessor:
    """
    A class to process and analyze performance data collected by the PerfTool.
    """

    @staticmethod
    def parse_perf_script(file_path: str) -> pd.DataFrame:
        """
        Parse the perf script output into a structured DataFrame.

        Args:
            file_path (str): Path to the perf script file.

        Returns:
            pd.DataFrame: Parsed data as a DataFrame.
        """
        data = []
        with open(file_path, "r") as file:
            for line in file:
                # Example parsing logic (adjust based on actual perf script format)
                if line.strip():
                    parts = line.split()
                    data.append({
                        "timestamp": parts[0],
                        "event": parts[1],
                        "details": " ".join(parts[2:]),
                    })
        return pd.DataFrame(data)

    @staticmethod
    def summarize_events(df: pd.DataFrame, event_column: str = "event") -> pd.DataFrame:
        """
        Summarize the frequency of events in the DataFrame.

        Args:
            df (pd.DataFrame): DataFrame containing perf script data.
            event_column (str): Column name for events.

        Returns:
            pd.DataFrame: Summary of event frequencies.
        """
        return df[event_column].value_counts().reset_index(name="count").rename(columns={"index": event_column})

if __name__ == "__main__":
    processor = PerfDataProcessor()

    # Example usage
    script_path = "./data/perf.script"
    parsed_data = processor.parse_perf_script(script_path)
    print("Parsed Data:")
    print(parsed_data.head())

    event_summary = processor.summarize_events(parsed_data)
    print("Event Summary:")
    print(event_summary)