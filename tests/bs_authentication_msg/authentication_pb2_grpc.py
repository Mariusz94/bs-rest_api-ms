# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bs_db_connector_msg import db_connector_pb2 as bs__db__connector__msg_dot_db__connector__pb2


class AuthenticationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/AuthenticationService/Login',
                request_serializer=bs__db__connector__msg_dot_db__connector__pb2.LoginData.SerializeToString,
                response_deserializer=bs__db__connector__msg_dot_db__connector__pb2.UserInfo.FromString,
                )


class AuthenticationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthenticationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=bs__db__connector__msg_dot_db__connector__pb2.LoginData.FromString,
                    response_serializer=bs__db__connector__msg_dot_db__connector__pb2.UserInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AuthenticationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthenticationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthenticationService/Login',
            bs__db__connector__msg_dot_db__connector__pb2.LoginData.SerializeToString,
            bs__db__connector__msg_dot_db__connector__pb2.UserInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
