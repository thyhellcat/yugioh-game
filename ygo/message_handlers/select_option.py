from gsb.intercepts import Menu

from twisted.internet import reactor

from ..card import Card
from ..parsers.duel_parser import DuelParser
from ..utils import process_duel
from .. import globals

def select_option(self, player, options):
  pl = self.players[player]
  def select(caller, idx):
    self.set_responsei(idx)
    reactor.callLater(0, process_duel, self)
  opts = []
  for opt in options:
    if opt > 10000:
      code = opt >> 4
      string = Card(code).get_strings(pl)[opt & 0xf]
    else:
      string = "Unknown option %d" % opt
      string = globals.strings[pl.language]['system'].get(opt, string)
    opts.append(string)
  m = Menu(pl._("Select option:"), no_abort=pl._("Invalid option."), persistent=True, prompt=pl._("Select option:"), restore_parser=DuelParser)
  for idx, opt in enumerate(opts):
    m.item(opt)(lambda caller, idx=idx: select(caller, idx))
  pl.notify(m)
