from .predeliverymiddleware import PreDeliveryMiddleware

middlewares = {
    'pre_delivery': PreDeliveryMiddleware
}


def get_middleware(name):
    return middlewares.get(name)


__all__ = ('PreDeliveryMiddleware', 'middlewares')
