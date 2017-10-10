# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import core_pb2 as core__pb2


class CoreRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListPods = channel.unary_unary(
        '/pb.CoreRPC/ListPods',
        request_serializer=core__pb2.Empty.SerializeToString,
        response_deserializer=core__pb2.Pods.FromString,
        )
    self.AddPod = channel.unary_unary(
        '/pb.CoreRPC/AddPod',
        request_serializer=core__pb2.AddPodOptions.SerializeToString,
        response_deserializer=core__pb2.Pod.FromString,
        )
    self.RemovePod = channel.unary_unary(
        '/pb.CoreRPC/RemovePod',
        request_serializer=core__pb2.RemovePodOptions.SerializeToString,
        response_deserializer=core__pb2.Empty.FromString,
        )
    self.GetPod = channel.unary_unary(
        '/pb.CoreRPC/GetPod',
        request_serializer=core__pb2.GetPodOptions.SerializeToString,
        response_deserializer=core__pb2.Pod.FromString,
        )
    self.AddNode = channel.unary_unary(
        '/pb.CoreRPC/AddNode',
        request_serializer=core__pb2.AddNodeOptions.SerializeToString,
        response_deserializer=core__pb2.Node.FromString,
        )
    self.RemoveNode = channel.unary_unary(
        '/pb.CoreRPC/RemoveNode',
        request_serializer=core__pb2.RemoveNodeOptions.SerializeToString,
        response_deserializer=core__pb2.Pod.FromString,
        )
    self.GetNode = channel.unary_unary(
        '/pb.CoreRPC/GetNode',
        request_serializer=core__pb2.GetNodeOptions.SerializeToString,
        response_deserializer=core__pb2.Node.FromString,
        )
    self.ListPodNodes = channel.unary_unary(
        '/pb.CoreRPC/ListPodNodes',
        request_serializer=core__pb2.ListNodesOptions.SerializeToString,
        response_deserializer=core__pb2.Nodes.FromString,
        )
    self.GetContainer = channel.unary_unary(
        '/pb.CoreRPC/GetContainer',
        request_serializer=core__pb2.ContainerID.SerializeToString,
        response_deserializer=core__pb2.Container.FromString,
        )
    self.GetContainers = channel.unary_unary(
        '/pb.CoreRPC/GetContainers',
        request_serializer=core__pb2.ContainerIDs.SerializeToString,
        response_deserializer=core__pb2.Containers.FromString,
        )
    self.ListNetworks = channel.unary_unary(
        '/pb.CoreRPC/ListNetworks',
        request_serializer=core__pb2.GetPodOptions.SerializeToString,
        response_deserializer=core__pb2.Networks.FromString,
        )
    self.SetNodeAvailable = channel.unary_unary(
        '/pb.CoreRPC/SetNodeAvailable',
        request_serializer=core__pb2.NodeAvailable.SerializeToString,
        response_deserializer=core__pb2.Node.FromString,
        )
    self.GetNodeByName = channel.unary_unary(
        '/pb.CoreRPC/GetNodeByName',
        request_serializer=core__pb2.GetNodeOptions.SerializeToString,
        response_deserializer=core__pb2.Node.FromString,
        )
    self.ContainerDeployed = channel.unary_unary(
        '/pb.CoreRPC/ContainerDeployed',
        request_serializer=core__pb2.ContainerDeployedOptions.SerializeToString,
        response_deserializer=core__pb2.Empty.FromString,
        )
    self.BuildImage = channel.unary_stream(
        '/pb.CoreRPC/BuildImage',
        request_serializer=core__pb2.BuildImageOptions.SerializeToString,
        response_deserializer=core__pb2.BuildImageMessage.FromString,
        )
    self.CreateContainer = channel.unary_stream(
        '/pb.CoreRPC/CreateContainer',
        request_serializer=core__pb2.DeployOptions.SerializeToString,
        response_deserializer=core__pb2.CreateContainerMessage.FromString,
        )
    self.RunAndWait = channel.stream_stream(
        '/pb.CoreRPC/RunAndWait',
        request_serializer=core__pb2.RunAndWaitOptions.SerializeToString,
        response_deserializer=core__pb2.RunAndWaitMessage.FromString,
        )
    self.RemoveContainer = channel.unary_stream(
        '/pb.CoreRPC/RemoveContainer',
        request_serializer=core__pb2.RemoveContainerOptions.SerializeToString,
        response_deserializer=core__pb2.RemoveContainerMessage.FromString,
        )
    self.ReallocResource = channel.unary_stream(
        '/pb.CoreRPC/ReallocResource',
        request_serializer=core__pb2.ReallocOptions.SerializeToString,
        response_deserializer=core__pb2.ReallocResourceMessage.FromString,
        )
    self.RemoveImage = channel.unary_stream(
        '/pb.CoreRPC/RemoveImage',
        request_serializer=core__pb2.RemoveImageOptions.SerializeToString,
        response_deserializer=core__pb2.RemoveImageMessage.FromString,
        )
    self.Backup = channel.unary_unary(
        '/pb.CoreRPC/Backup',
        request_serializer=core__pb2.BackupOptions.SerializeToString,
        response_deserializer=core__pb2.BackupMessage.FromString,
        )


class CoreRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListPods(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPod(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemovePod(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPod(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddNode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveNode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPodNodes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetContainer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetContainers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListNetworks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetNodeAvailable(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNodeByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerDeployed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BuildImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateContainer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunAndWait(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveContainer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReallocResource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Backup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CoreRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListPods': grpc.unary_unary_rpc_method_handler(
          servicer.ListPods,
          request_deserializer=core__pb2.Empty.FromString,
          response_serializer=core__pb2.Pods.SerializeToString,
      ),
      'AddPod': grpc.unary_unary_rpc_method_handler(
          servicer.AddPod,
          request_deserializer=core__pb2.AddPodOptions.FromString,
          response_serializer=core__pb2.Pod.SerializeToString,
      ),
      'RemovePod': grpc.unary_unary_rpc_method_handler(
          servicer.RemovePod,
          request_deserializer=core__pb2.RemovePodOptions.FromString,
          response_serializer=core__pb2.Empty.SerializeToString,
      ),
      'GetPod': grpc.unary_unary_rpc_method_handler(
          servicer.GetPod,
          request_deserializer=core__pb2.GetPodOptions.FromString,
          response_serializer=core__pb2.Pod.SerializeToString,
      ),
      'AddNode': grpc.unary_unary_rpc_method_handler(
          servicer.AddNode,
          request_deserializer=core__pb2.AddNodeOptions.FromString,
          response_serializer=core__pb2.Node.SerializeToString,
      ),
      'RemoveNode': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveNode,
          request_deserializer=core__pb2.RemoveNodeOptions.FromString,
          response_serializer=core__pb2.Pod.SerializeToString,
      ),
      'GetNode': grpc.unary_unary_rpc_method_handler(
          servicer.GetNode,
          request_deserializer=core__pb2.GetNodeOptions.FromString,
          response_serializer=core__pb2.Node.SerializeToString,
      ),
      'ListPodNodes': grpc.unary_unary_rpc_method_handler(
          servicer.ListPodNodes,
          request_deserializer=core__pb2.ListNodesOptions.FromString,
          response_serializer=core__pb2.Nodes.SerializeToString,
      ),
      'GetContainer': grpc.unary_unary_rpc_method_handler(
          servicer.GetContainer,
          request_deserializer=core__pb2.ContainerID.FromString,
          response_serializer=core__pb2.Container.SerializeToString,
      ),
      'GetContainers': grpc.unary_unary_rpc_method_handler(
          servicer.GetContainers,
          request_deserializer=core__pb2.ContainerIDs.FromString,
          response_serializer=core__pb2.Containers.SerializeToString,
      ),
      'ListNetworks': grpc.unary_unary_rpc_method_handler(
          servicer.ListNetworks,
          request_deserializer=core__pb2.GetPodOptions.FromString,
          response_serializer=core__pb2.Networks.SerializeToString,
      ),
      'SetNodeAvailable': grpc.unary_unary_rpc_method_handler(
          servicer.SetNodeAvailable,
          request_deserializer=core__pb2.NodeAvailable.FromString,
          response_serializer=core__pb2.Node.SerializeToString,
      ),
      'GetNodeByName': grpc.unary_unary_rpc_method_handler(
          servicer.GetNodeByName,
          request_deserializer=core__pb2.GetNodeOptions.FromString,
          response_serializer=core__pb2.Node.SerializeToString,
      ),
      'ContainerDeployed': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerDeployed,
          request_deserializer=core__pb2.ContainerDeployedOptions.FromString,
          response_serializer=core__pb2.Empty.SerializeToString,
      ),
      'BuildImage': grpc.unary_stream_rpc_method_handler(
          servicer.BuildImage,
          request_deserializer=core__pb2.BuildImageOptions.FromString,
          response_serializer=core__pb2.BuildImageMessage.SerializeToString,
      ),
      'CreateContainer': grpc.unary_stream_rpc_method_handler(
          servicer.CreateContainer,
          request_deserializer=core__pb2.DeployOptions.FromString,
          response_serializer=core__pb2.CreateContainerMessage.SerializeToString,
      ),
      'RunAndWait': grpc.stream_stream_rpc_method_handler(
          servicer.RunAndWait,
          request_deserializer=core__pb2.RunAndWaitOptions.FromString,
          response_serializer=core__pb2.RunAndWaitMessage.SerializeToString,
      ),
      'RemoveContainer': grpc.unary_stream_rpc_method_handler(
          servicer.RemoveContainer,
          request_deserializer=core__pb2.RemoveContainerOptions.FromString,
          response_serializer=core__pb2.RemoveContainerMessage.SerializeToString,
      ),
      'ReallocResource': grpc.unary_stream_rpc_method_handler(
          servicer.ReallocResource,
          request_deserializer=core__pb2.ReallocOptions.FromString,
          response_serializer=core__pb2.ReallocResourceMessage.SerializeToString,
      ),
      'RemoveImage': grpc.unary_stream_rpc_method_handler(
          servicer.RemoveImage,
          request_deserializer=core__pb2.RemoveImageOptions.FromString,
          response_serializer=core__pb2.RemoveImageMessage.SerializeToString,
      ),
      'Backup': grpc.unary_unary_rpc_method_handler(
          servicer.Backup,
          request_deserializer=core__pb2.BackupOptions.FromString,
          response_serializer=core__pb2.BackupMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pb.CoreRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
