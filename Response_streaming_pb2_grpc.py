# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Response_streaming_pb2 as Response__streaming__pb2


class rsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.numbers = channel.unary_stream(
        '/rs/numbers',
        request_serializer=Response__streaming__pb2.number.SerializeToString,
        response_deserializer=Response__streaming__pb2.square.FromString,
        )


class rsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def numbers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_rsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'numbers': grpc.unary_stream_rpc_method_handler(
          servicer.numbers,
          request_deserializer=Response__streaming__pb2.number.FromString,
          response_serializer=Response__streaming__pb2.square.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rs', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
