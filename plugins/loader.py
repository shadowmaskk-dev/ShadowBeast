import importlib
import os

plugins = []


def load_plugins():

    global plugins

    plugins.clear()

    for file in os.listdir(
        "plugins"
    ):

        if (
            file.endswith(".py")
            and file not in (
                "__init__.py",
                "loader.py"
            )
        ):

            module_name = (
                f"plugins.{file[:-3]}"
            )

            try:

                if module_name in importlib.sys.modules:

                    module = importlib.reload(
                        importlib.sys.modules[
                            module_name
                        ]
                    )

                else:

                    module = importlib.import_module(
                        module_name
                    )

                plugins.append(
                    module
                )

            except Exception as e:

                print(
                    f"Failed to load "
                    f"{file}: {e}"
                )


def handle_plugin(
    command
):

    for plugin in plugins:

        try:

            if plugin.handle(
                command
            ):

                return True

        except Exception as e:

            print(
                f"Plugin Error: {e}"
            )

    return False


def get_plugins():

    return [
        plugin.__name__.split(
            "."
        )[-1]
        for plugin in plugins
    ]
