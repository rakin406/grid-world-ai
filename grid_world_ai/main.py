from render_system import RenderSystem
import pecs


def run():
    registry = pecs.Registry()
    render_system = RenderSystem(registry)
    render_system.display()


if __name__ == "__main__":
    run()
