from autobahn.asyncio.websocket import WampWebSocketServerProtocol, \
    WebSocketServerFactory


class MyServerProtocol(WampWebSocketServerProtocol):

    def onConnect(self, request):
        pass

    def onOpen(self):
        pass

    def onMessage(self, payload, isBinary):
        pass
        # data = self.data
        # if data.get('text', None):
        #     result_pages = Page.objects.search_text(
        #         text=data.get('text', None)
        #     )
        #     logging.info('It form message for send mail.')
        #     str_message = '<div>'
        #     for page in result_pages:
        #         str_message += '<div style="margin-bottom: 10px; ' \
        #                        'border-bottom: 1px solid black">'
        #         str_message += '<p>Автор: {}</p>'.format(page.book.author)
        #         str_message += '<p>Книга: {}</p>'.format(page.book.name_book)
        #         str_message += '<p>Часть: {}</p>'.format(page.part)
        #         str_message += '<p>Раздел: {}</p>'.format(page.section)
        #         str_message += '<p>Глава: {}</p>'.format(page.chapter)
        #         str_message += '<p>Страница: {}</p>'.format(page.page_number)
        #         str_message += '</div>'
        #     str_message += '</div>'
        #     return self.send_email(text=str_message,
        #                            to=data.get('email', None))
        # else:
        #     return False

    def onClose(self, wasClean, code, reason):
        pass


if __name__ == '__mail__':
    import asyncio

    factory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    factory.protocol = MyServerProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '0.0.0.0', 9000)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
    loop.close()
