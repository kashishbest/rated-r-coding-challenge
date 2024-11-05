from dataclasses import dataclass

@dataclass
class Stats:
    total_successful_requests: int
    total_failed_requests: int
    uptime: float
    average_latency: float
    median_latency: float
    p99_latency: float

@dataclass
class StatsResponse:
    customer_id: str
    from_date: str
    stats: Stats
