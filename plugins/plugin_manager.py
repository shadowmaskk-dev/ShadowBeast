from plugins.loader import (
    load_plugins,
    get_plugins
)


def handle(command):

    lower = command.lower()

    if lower == "plugins":

        loaded = get_plugins()

        print(
            "\nLoaded Plugins:\n"
        )

        for plugin in loaded:

            print(
                "-",
                plugin
            )

        return True

    if lower == "reload":

        load_plugins()

        print(
            "\nPlugins reloaded."
        )

        return True

    return False
