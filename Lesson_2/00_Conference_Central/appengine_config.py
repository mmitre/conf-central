def webapp_add_wsgi_middleware(app):
  from google.appengine.ext.appstats import recording
  appstats_CALC_RPC_COSTS = True
  app = recording.appstats_wsgi_middleware(app)
  return app