

import logging

logger = logging.getLogger(__name__)


class ExecutorLogger:
    def info(self, text):
        pass  # interface method

    def log(self, text):
        pass  # interface method

    def error(self, text):
        pass  # interface method

    def end(self):
        pass  # interface method


class ConsoleExecutorLogger(ExecutorLogger):
    def info(self, text):
        print(text)

    def log(self, text):
        print(text)

    def error(self, text):
        print(text)


class FileExecutorLogger(ExecutorLogger):
    def __init__(self, stdout_path, stderr_path):
        logger.debug("Write stdout to {:s}".format(stdout_path))
        logger.debug("Write stderr to {:s}".format(stderr_path))
        self.stdout_path = stdout_path
        self.stderr_path = stderr_path
        self.stdout = ""
        self.stderr = ""

    def info(self, text):
        self.stdout += text + "\n"

    def log(self, text):
        self.stdout += text + "\n"

    def error(self, text):
        if self.stdout_path != self.stderr_path:
            self.stderr += text + "\n"
        else:
            self.stdout += text + "\n"

    def end(self):
        with open(self.stdout_path, "w") as file:
            file.write(self.stdout)

        if self.stdout_path != self.stderr_path:
            with open(self.stderr_path, "w") as file:
                file.write(self.stderr)
