import subprocess
from typing import List, Optional

class PerfTool:
    """
    A class to interact with the perf tool using Python bindings.
    """

    def __init__(self, output_dir: str = "./data"):
        self.output_dir = output_dir

    def record(self, events: List[str], frequency: int, duration: Optional[int] = None):
        """
        Record performance data using perf.

        Args:
            events (List[str]): List of events to record.
            frequency (int): Sampling frequency.
            duration (Optional[int]): Duration of the recording in seconds.
        """
        command = [
            "perf", "record",
            "-e", ",".join(events),
            "-F", str(frequency),
            "-o", f"{self.output_dir}/perf.data",
            "--",
            "sleep", str(duration) if duration else "10"
        ]
        subprocess.run(command, check=True)

    def script(self):
        """
        Generate a perf script from the recorded data.
        """
        command = [
            "perf", "script",
            "-i", f"{self.output_dir}/perf.data",
            "-o", f"{self.output_dir}/perf.script"
        ]
        subprocess.run(command, check=True)

    def stat(self, events: List[str], duration: Optional[int] = None):
        """
        Collect performance statistics using perf.

        Args:
            events (List[str]): List of events to monitor.
            duration (Optional[int]): Duration of the monitoring in seconds.
        """
        command = [
            "perf", "stat",
            "-e", ",".join(events),
            "--",
            "sleep", str(duration) if duration else "10"
        ]
        subprocess.run(command, check=True)

if __name__ == "__main__":
    perf_tool = PerfTool(output_dir="./data")
    events = ["cycles", "instructions", "branch-misses"]

    # Record data
    perf_tool.record(events=events, frequency=999, duration=10)

    # Generate script
    perf_tool.script()

    # Collect statistics
    perf_tool.stat(events=events, duration=10)