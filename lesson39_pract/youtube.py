import psycopg
from psycopg.rows import dict_row, class_row

from dataclasses import dataclass

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "youtube_db",
    "user": "postgres",
    "password": "12345",
}


@dataclass(slots=True)
class Channel:
    id: int | None
    channel_name: str
    subscribers_count: int
    monthly_views: int


@dataclass(slots=True)
class Video:
    id: int | None
    video_title: str
    duration_seconds: int
    views_count: int
    likes_count: int
    dislikes_count: int
    channel_id: int
    channel: Channel | None = None


def get_connection():
    return psycopg.connect(**DB_CONFIG)


def get_all_videos(conn) -> list[Video]:
    with conn.cursor(row_factory=class_row(Video)) as cur:

        cur.execute("""
                    SELECT 
                    id,
                    video_title,
                    duration_seconds,
                    views_count,
                    likes_count,
                    dislikes_count,
                    channel_id
                    FROM videos 
                    ORDER BY id ASC
                    """)

        return list(cur.fetchall())


def get_all_channels(conn) -> list[Channel]:
    with conn.cursor(row_factory=class_row(Channel)) as cur:

        cur.execute("""
                    SELECT 
                    id,
                    channel_name,
                    subscribers_count,
                    monthly_views
                    FROM channels 
                    ORDER BY id ASC
                    """)

        return list(cur.fetchall())


def get_all_videos_with_channels(conn) -> list[Video]:
    videos_list = []

    with conn.cursor(row_factory=dict_row) as cur:

        cur.execute(""" 
                    SELECT
                    v.id AS video_id,
                    v.video_title,
                    v.duration_seconds,
                    v.views_count,
                    v.likes_count,
                    v.dislikes_count,

                    c.id AS channel_id,
                    c.channel_name,
                    c.subscribers_count,
                    c.monthly_views
                    FROM videos AS v
                    
                    INNER JOIN channels AS c
                    ON v.channel_id = c.id
                        
                    ORDER BY v.id;
                    """)

        rows = cur.fetchall()

        for row in rows:
            new_channel = Channel(
                id=row["channel_id"],
                channel_name=row["channel_name"],
                subscribers_count=row["subscribers_count"],
                monthly_views=row["monthly_views"],
            )

            new_videos = Video(
                id=row["video_id"],
                video_title=row["video_title"],
                duration_seconds=row["duration_seconds"],
                views_count=row["views_count"],
                likes_count=row["likes_count"],
                dislikes_count=row["dislikes_count"],
                channel_id=row["channel_id"],
                channel=new_channel,
            )

            videos_list.append(new_videos)

    return videos_list


def value_to_str(value):
    if value is None:
        return "-"
    return str(value)


def print_channels(channels: list[Channel]):
    print("Каналы:")

    print(
        f"{'ID':<5}"
        f"{'CHANNEL NAME':<25}"
        f"{'SUBSCRIBERS':<15}"
        f"{'MONTHLY VIEWS':<15}"
    )

    for channel in channels:
        print(
            f"{value_to_str(channel.id):<5}"
            f"{channel.channel_name:<25}"
            f"{channel.subscribers_count:<15}"
            f"{channel.monthly_views:<15}"
        )


def print_videos(videos: list[Video]):
    print("Видео:")

    print(
        f"{'ID':<5}"
        f"{'VIDEO TITLE':<40}"
        f"{'DURATION':<12}"
        f"{'VIEWS':<12}"
        f"{'LIKES':<10}"
        f"{'DISLIKES':<12}"
        f"{'CHANNEL ID':<12}"
    )

    for video in videos:
        print(
            f"{value_to_str(video.id):<5}"
            f"{video.video_title:<40}"
            f"{video.duration_seconds:<12}"
            f"{video.views_count:<12}"
            f"{video.likes_count:<10}"
            f"{video.dislikes_count:<12}"
            f"{video.channel_id:<12}"
        )


def print_videos_with_channels(videos: list[Video]):
    print("Видео вместе с каналами:")

    print(
        f"{'ID':<5}"
        f"{'VIDEO TITLE':<40}"
        f"{'DURATION':<12}"
        f"{'VIEWS':<12}"
        f"{'LIKES':<10}"
        f"{'DISLIKES':<12}"
        f"{'CHANNEL ID':<12}"
        f"{'CHANNEL NAME':<25}"
        f"{'SUBSCRIBERS':<15}"
        f"{'MONTHLY VIEWS':<15}"
    )

    for video in videos:
        print(
            f"{value_to_str(video.id):<5}"
            f"{video.video_title:<40}"
            f"{video.duration_seconds:<12}"
            f"{video.views_count:<12}"
            f"{video.likes_count:<10}"
            f"{video.dislikes_count:<12}"
            f"{video.channel_id:<12}"
            f"{video.channel.channel_name:<25}"
            f"{video.channel.subscribers_count:<15}"
            f"{video.channel.monthly_views:<15}"
        )


with get_connection() as conn:
    videos = get_all_videos(conn)
    channels = get_all_channels(conn)

    videos_with_channels = get_all_videos_with_channels(conn)

    print_videos(videos)

    print("\n" + "*" * 50 + "\n")

    print_channels(channels)

    print("\n" + "*" * 50 + "\n")

    print_videos_with_channels(videos_with_channels)
