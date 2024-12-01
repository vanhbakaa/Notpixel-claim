from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [2700, 4200]
    DELAY_EACH_ACCOUNT: list[int] = [15, 25]
    START_DELAY: list[int] = [5, 100]
    AUTO_TASK: bool = True
    USE_PUMPKIN_BOMB: bool = False
    TASKS_TO_DO: list[str] = ["paint20pixels", "x:notpixel", "x:notcoin", "channel:notcoin", "channel:notpixel_channel"
                                ,"joinSquad", "jettonTask", "pumpkin", "pixelInNickname"]
    AUTO_DRAW: bool = False
    JOIN_TG_CHANNELS: bool = False
    CLAIM_REWARD: bool = True
    AUTO_UPGRADE: bool = False
    REF_ID: str = 'f6624523270'
    IGNORED_BOOSTS: list[str] = []
    IN_USE_SESSIONS_PATH: str = 'bot/config/used_sessions.txt'
    NIGHT_MODE: bool = False
    NIGHT_TIME: list[int] = [0, 7] #UTC HOURS
    NIGHT_CHECKING: list[int] = [3600, 7200]
    ENERGY_LIMIT_MAX_LEVEL: int = 1
    PAINT_REWARD_MAX_LEVEL: int = 1
    RECHARGE_SPEED_MAX_LEVEL: int = 1
    ADVANCED_ANTI_DETECTION: bool = True

    ENABLE_SSL: bool = True

    USE_PROXIES_FROM_FILE: bool = False


settings = Settings()
