#!/usr/bin/env python3

from enum import Enum

class OfpType(Enum):
  # Immutable messages.
  OFPT_HELLO                    = 0   # Symmetric message
  OFPT_ERROR                    = 1   # Symmetric message
  OFPT_ECHO_REQUEST             = 2   # Symmetric message
  OFPT_ECHO_REPLY               = 3   # Symmetric message
  OFPT_VENDOR                   = 4   # Symmetric message
  # Switch configuration messages.
  OFPT_FEATURES_REQUEST         = 5   # Controller/switch message
  OFPT_FEATURES_REPLY           = 6   # Controller/switch message
  OFPT_GET_CONFIG_REQUEST       = 7   # Controller/switch message
  OFPT_GET_CONFIG_REPLY         = 8   # Controller/switch message
  OFPT_SET_CONFIG               = 9   # Controller/switch message
  # Asynchronous messages.
  OFPT_PACKET_IN                = 10  # Async message
  OFPT_FLOW_REMOVED             = 11  # Async message
  OFPT_PORT_STATUS              = 12  # Async message
  # Controller command messages.
  OFPT_PACKET_OUT               = 13  # Controller/switch message
  OFPT_FLOW_MOD                 = 14  # Controller/switch message
  OFPT_PORT_MOD                 = 15  # Controller/switch message
  # Statistics messages.
  OFPT_STATS_REQUEST            = 16  # Controller/switch message
  OFPT_STATS_REPLY              = 17  # Controller/switch message
  # Barrier messages.
  OFPT_BARRIER_REQUEST          = 18  # Controller/switch message
  OFPT_BARRIER_REPLY            = 19  # Controller/switch message
  # Queue Configuration messages.
  OFPT_QUEUE_GET_CONFIG_REQUEST = 20  # Controller/switch message
  OFPT_QUEUE_GET_CONFIG_REPLY   = 21  # Controller/switch message

# Header on all OpenFlow packets.
class OfpHeader(object):
  # version  uint8_t:  OFP_VERSION.
  # type     uint8_t:  One of the OFPT_ constants.
  # length   uint16_t: Length including this ofp_header.
  # xid      uint32_t: Transaction id associated with this packet.
  #                    Replies use the same id as was in the request
  #                    to facilitate pairing.

  def __init__(self, filename):
    with open(filename, mode='rb') as f:
      self.version = f.read(1)
      self.type = f.read(1)
      self.length = f.read(2)
      self.xid = f.read(4)

  @staticmethod
  def to_int(value):
    return int.from_bytes(value, byteorder='big', signed=False)

  def __str__(self):
    return "OpenFlow protocol message:\n - version: {v}\n - type: {t} ({t_name})\n - length: {l}\n - xid: {x}".format(
      v = self.to_int(header.version),
      t = self.to_int(header.type),
      t_name = OfpType(self.to_int(header.type)).name,
      l = self.to_int(header.length),
      x = self.to_int(header.xid)
    )

header = OfpHeader('ofpt_hello.dat')
print(header)
