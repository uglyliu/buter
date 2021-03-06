from buter.logger import LOG
from buter.server import create_app

app, config = create_app()

if __name__ == '__main__':
    #
    # 打印 url rule ：werkzeug.routing.Rule
    # 格式参考 Spring Mvc：
    # Mapped "{[/manage/account/{id}],methods=[GET]}"
    #   onto public T com.zeus.web.controller.AbstractController.get(java.lang.Long)
    #
    for rule in app.url_map.iter_rules():
        LOG.info("Mapped {:30} methods={:30} onto {}".format(rule.rule, ', '.join(rule.methods), rule.endpoint))

    app.run(
        host=config.SERVER_HOST,
        port=config.SERVER_PORT,
        debug=config.DEBUG,
        use_reloader=config.USE_RELOADER,
        ssl_context=config.HTTPS
    )
