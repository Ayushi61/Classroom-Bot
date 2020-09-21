from rest_framework.response import Response


class BaseMiddleWare(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)


class ValidateTeamIDMiddleware(BaseMiddleWare):

    def process_request(self, request):

        data = request.data

        if "team_id" not in data:
            return Response(data={
                                "status": 1,
                                "message": "Missing team_id in the request from the slack.",
                                "data": []
                            })
