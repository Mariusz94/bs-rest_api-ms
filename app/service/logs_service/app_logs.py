import logging
import config


def init_logging() -> None:
    """
    Konfiguracja logera.

    Returns:
        None
    """
    logging.basicConfig(
        level=getattr(logging, config.LOGGING_MODE),
        format="%(asctime)s.%(msecs)03d-%(levelname)s-%(funcName)s()-%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.info("SET UP FINISHED\n")


def config_logs() -> None:
    """
    Logi pojawiające się przy uruchomieniu mikroserwisu.

    Returns:
        None
    """
    logging.info(f"{config.SERVICE_NAME=}")
    logging.info(f"{config.MS_VERSION=}")
    logging.info(f"{config.SERVICE_PORT=}")
    logging.info(f"{config.LOGGING_MODE=}")
    logging.info("\n")
