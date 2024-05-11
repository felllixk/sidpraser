from app.app import App
from app.kernel import Kernel
from controllers.ParserController import ParserController


def main():
    kernel = Kernel()
    App.setKernel(kernel)
    App.run()


if __name__ == "__main__":
    main()
