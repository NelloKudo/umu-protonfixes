"""Wuthering Waves - ID 3513350
https://www.protondb.com/app/3513350
"""

from protonfixes import util
from pathlib import Path

def main() -> None:
    """Font fixes for in-game resources, if any."""
    util.protontricks('sourcehansans')
    util.protontricks('fakechinese')
    util.protontricks('corefonts')

    """As of version 3.4, SteamOS/SteamDeck env vars force a broken plugin in-game to play videos."""
    """Unsetting them to also prevent issues on Steam Decks where they are set by default."""
    util.del_environment('SteamOS')
    util.del_environment('SteamDeck')

    """As of version 3.8, in-game web pages stay white with KRWebClient.exe due to missing dcomp."""
    """Force its bitmap fallback."""
    for exe in Path(util.get_game_install_path()).glob('**/KRSDKWebViewOSR/KRWebClient.exe'):
	    exe.with_name('usebitmap.flag').touch()
