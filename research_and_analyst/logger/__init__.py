from .custom_logger import CustomLogger
# Create a single shared logger instance
GLOBAL_LOGGER = CustomLogger().get_logger("research_and_analyst")
from logger.custom_logger import CustomLogger


GLOBAL_LOGGER = CustomLogger().get_logger(__name__)


__all__ = ["CustomLogger", "GLOBAL_LOGGER"]
