#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update i18n JSON files with complete Chinese and English translations, and build Lua data."""

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from i18n_data_ui import UI_ZH, DIALOGS_ZH
from i18n_data_perf1 import PERF1_ZH
from i18n_data_perf2 import PERF2_ZH
from i18n_data_perf3 import PERF3_ZH
from i18n_data_perf4 import PERF4_ZH
from i18n_data_vis import VIS_ZH
from i18n_data_tools import TOOLS_ZH


def main():
    # 1. Load extracted 404 options
    extracted_path = ROOT / "build/extracted_options.json"
    if not extracted_path.exists():
        print("ERROR: build/extracted_options.json not found", file=sys.stderr)
        sys.exit(1)

    with open(extracted_path, "r", encoding="utf-8") as f:
        all_options = json.load(f)

    # 2. Load existing zh_cn.json and en_us.json
    zh_path = ROOT / "i18n/zh_cn.json"
    en_path = ROOT / "i18n/en_us.json"

    with open(zh_path, "r", encoding="utf-8") as f:
        zh_data = json.load(f)

    with open(en_path, "r", encoding="utf-8") as f:
        en_data = json.load(f)

    # Combine all translated chunks
    all_translated = {}
    all_translated.update(PERF1_ZH)
    all_translated.update(PERF2_ZH)
    all_translated.update(PERF3_ZH)
    all_translated.update(PERF4_ZH)
    all_translated.update(VIS_ZH)
    all_translated.update(TOOLS_ZH)

    # 3. Assemble zh_cn.json options
    zh_options = zh_data.get("options", {})
    # For every option in all_options, if we have a translation in all_translated, use it
    # If it was already in zh_options and had label/tip, preserve it if not overridden
    for opt in all_options:
        key = opt["key"]
        if key in all_translated:
            zh_options[key] = all_translated[key]
        elif key in zh_options:
            pass  # keep existing
        else:
            print(f"WARNING: Option {key} has no translation!", file=sys.stderr)

    zh_data["ui"] = UI_ZH
    zh_data["dialogs"] = DIALOGS_ZH
    zh_data["options"] = zh_options

    # 4. Assemble en_us.json
    # Create complete options dictionary for English
    en_options = {}
    for opt in all_options:
        key = opt["key"]
        en_options[key] = {
            "label": opt["label"],
            "tip": opt["tip"]
        }

    # UI chrome for en_us
    UI_EN = {
        "tabs": {
            "pzopt": "PZ Optimization",
            "optimizations": "Optimizations",
            "enhancements": "Enhancements",
            "profiler": "Profiler"
        },
        "views": {
            "label": "View",
            "simple": "Simple",
            "advanced": "Advanced",
            "everything": "Everything"
        },
        "view_tips": {
            "simple": "The settings worth knowing about: the features and the main switches.",
            "advanced": "Also the settings that change how something is done; the defaults are what was measured best.",
            "everything": "Also the tuning numbers (budgets, thread counts, intervals). Change them to experiment."
        },
        "notes": {
            "restart": "Takes effect on the next launch.",
            "live": "Applies as soon as you press Apply; no restart needed.",
            "home_note": "Apply or Accept saves your changes to Zomboid/pzopt/options.ini. Performance settings take effect on the next launch; Visuals and Tools apply at once (a few Visuals on the next launch). Settings pinned by the game folder's pzopt.properties or -Dpzopt.<key> cannot be changed here."
        },
        "masters": {
            "enabled_label": "Optimizations enabled (master switch)",
            "enabled_tip": "Off = the game runs stock: every override takes its original code path and the settings below are ignored. On = the settings below apply. The Tools are not affected: the performance overlay works either way.",
            "enhancements_label": "Enhancements enabled (master switch)",
            "enhancements_tip": "Off = the picture is the stock game's: upscaling, sprite filtering, HDR output, ambient occlusion, sun shadows, reflections, car glass, the darkness floor, remembered places, colour grading, per-pixel lighting, god rays and foliage sway are all off. On = the settings below apply.",
            "profiler_label": "Profiler enabled (master switch)",
            "profiler_tip": "Off = no performance overlay, no measuring and no frame log: the overlay's samplers never start and the toggle key only says the profiler is off. On = the settings below apply."
        },
        "groups": {
            "perf": {
                "title": "Performance",
                "note": "Smoother frames and faster loads. Nothing here changes how the game looks."
            },
            "vis": {
                "title": "Visuals",
                "note": "Graphics the stock game does not have. Off by default; each card says what it costs."
            },
            "tools": {
                "title": "Tools",
                "note": "The performance overlay (F9), its game-thread profiler and the console log."
            }
        },
        "categories": {
            "smooth": {
                "title": "Smoothness and pacing",
                "blurb": "Even frame delivery, variable refresh and input latency."
            },
            "drive": {
                "title": "Driving",
                "blurb": "The car's stutter and rubber banding, and the world arriving at speed."
            },
            "world": {
                "title": "World drawing",
                "blurb": "What the chunk pictures hold and how many are drawn in a frame."
            },
            "weather": {
                "title": "Lighting, cutaways and weather",
                "blurb": "Light refreshes, see-through walls and roofs, fog, rain and puddles."
            },
            "zombies": {
                "title": "Zombies and hordes",
                "blurb": "The zombie simulation spread over every core, and cheaper checks."
            },
            "load": {
                "title": "Boot and loading",
                "blurb": "From launch to the menu, and from Continue to the world."
            },
            "ui": {
                "title": "Menus, inventory and map",
                "blurb": "Windows that answer in the frame you click."
            },
            "system": {
                "title": "System, sound and mods",
                "blurb": "Cores and power, the audio mix, other mods, updates."
            },
            "image": {
                "title": "Image quality",
                "blurb": "Upscalers, dynamic resolution, sprite filtering and HDR output."
            },
            "light": {
                "title": "Lighting and shadows",
                "blurb": "Per-pixel light, the real sky's shadows, ambient occlusion and god rays."
            },
            "refl": {
                "title": "Reflections and glass",
                "blurb": "Water and puddles, mirrors and windows, car glass, wet blood."
            },
            "atmos": {
                "title": "Atmosphere and detail",
                "blurb": "Darkness and colour grading, foliage sway, relief, zombie outlines."
            },
            "overlay": {
                "title": "Performance overlay",
                "blurb": "Frame times, utilization and what the game thread does, on screen."
            }
        },
        "subcategories": {
            "Frame pacing": "Frame pacing",
            "Variable refresh": "Variable refresh",
            "Input latency": "Input latency",
            "Car smoothness": "Car smoothness",
            "Chunk streaming": "Chunk streaming",
            "Render distance": "Render distance",
            "Trees while driving": "Trees while driving",
            "What bakes": "What bakes",
            "Bake budgets": "Bake budgets",
            "Zoom": "Zoom",
            "Blood and flies": "Blood and flies",
            "Sprite buffers": "Sprite buffers",
            "Lighting": "Lighting",
            "Cutaways": "Cutaways",
            "Fog": "Fog",
            "Rain and puddles": "Rain and puddles",
            "On other cores": "On other cores",
            "Cheaper checks": "Cheaper checks",
            "Detail by distance": "Detail by distance",
            "Loading screen": "Loading screen",
            "Boot": "Boot",
            "Files and textures": "Files and textures",
            "Windows": "Windows",
            "Map": "Map",
            "Lua": "Lua",
            "Cores and power": "Cores and power",
            "Sound": "Sound",
            "Mods and multiplayer": "Mods and multiplayer",
            "Updates": "Updates",
            "Upscaling": "Upscaling",
            "Dynamic resolution": "Dynamic resolution",
            "Sprite filtering": "Sprite filtering",
            "HDR output": "HDR output",
            "Per-pixel lighting": "Per-pixel lighting",
            "Sun, moon and clouds": "Sun, moon and clouds",
            "Ambient occlusion": "Ambient occlusion",
            "God rays": "God rays",
            "Water and puddles": "Water and puddles",
            "Mirrors and windows": "Mirrors and windows",
            "Car glass": "Car glass",
            "Wet blood": "Wet blood",
            "Darkness and grading": "Darkness and grading",
            "Foliage sway": "Foliage sway",
            "Relief": "Relief",
            "Zombie outlines": "Zombie outlines",
            "Overlay": "Overlay",
            "Fps colour": "Fps colour",
            "Console log": "Console log",
            "More": "More"
        },
        "buttons": {
            "home": "<  Home",
            "help": "HELP",
            "fix_problem": "Fix a problem",
            "show_more": "Show more",
            "show_more_tip": "Switches the view so this subcategory shows the rest of its settings.",
            "export": "Export settings",
            "export_tip": "Copies the settings of the Optimizations, Enhancements and Profiler tabs to the clipboard as text and saves to Zomboid/pzopt/settings-export.ini",
            "import": "Import settings...",
            "import_tip": "Sets the controls of the tabs from exported text",
            "uninstall": "Uninstall PZ Optimization...",
            "compat": "Mod compatibility check",
            "compat_tip": "Checks for conflicts between active Java mods and PZ Optimization.",
            "update": "Check for updates",
            "update_tip": "Checks for updates and opens the PZ Optimization updater dialog.",
            "overlay": "Performance overlay",
            "overlay_tip": "Toggles the performance overlay (F9 / L3 + R3).",
            "restart": "Restart game",
            "close": "Close",
            "apply": "Apply",
            "accept": "Accept",
            "cancel": "Cancel",
            "reset_group": "Reset group to defaults",
            "reset_category": "Reset category to defaults",
            "reset_category_tip": "Puts every setting of this category back to the build's default on this machine. Only the controls change; Apply or Accept saves them."
        },
        "presets": {
            "label": "Presets",
            "recommended": "Recommended defaults",
            "recommended_tip": "Reset to recommended balanced parameters",
            "recommended_btn": "Recommended (every optimization on)",
            "recommended_tip_long": "Turns the Performance master switch on and puts every Performance setting back to the build's default on this machine. Visuals and Tools are not changed. Takes effect on the next launch.",
            "stock": "Stock game",
            "stock_tip": "Disable all optimizations, restoring vanilla behavior",
            "stock_btn": "Stock game (every optimization off)",
            "stock_tip_long": "Turns the Performance master switch off: the game runs its original code everywhere, as if the overrides were not installed. The settings are kept for when you turn it on again; Tools and the performance overlay are not affected. Takes effect on the next launch.",
            "low_end": "Low-end hardware",
            "low_end_btn": "Low-end hardware (4 cores or less)",
            "low_end_tip": "A locked 60 fps on a 4-core CPU with an old GPU: turns the master switch on, a render distance of 9 chunks, no chunk worker pool, trees baked only while walking, vsync on with frame limit at 60, lighting updates 10/s, UI redrawn 30/s and texture compression. Takes effect on the next launch."
        },
        "pills": {
            "advanced": "ADVANCED",
            "expert": "EXPERT",
            "changed": "CHANGED",
            "next_launch": "next launch",
            "pinned": "pinned",
            "mod_off": "off for a mod"
        },
        "crumbs": {
            "home": "Home",
            "problems": "Help  >  Fix a problem",
            "search": "Search",
            "overview": "Overview"
        },
        "help": {
            "hint": "Not sure what to change? Start from what you notice.",
            "problem_desc": "Stutter while driving, low fps in a horde, slow loading, laggy input... Pick what you notice: why it happens, and the settings that help.",
            "fix_subtitle": "Pick what you notice: why it happens, and the settings that help, wherever they live."
        },
        "clips": {
            "label": "Before / after clips",
            "tip": "Plays a short clip of the stock game and one with the setting on, side by side, above the description of the setting under the mouse. Off saves the memory the clips take (up to ~100 MB of video memory while this screen is open). Applies at once and is remembered."
        },
        "status": {
            "on_changed": "{on} on, {changed} changed",
            "on": "{on} on",
            "changed": "{changed} changed",
            "off": "Off",
            "off_lower": "off",
            "recommended": "Recommended"
        },
        "framecap": {
            "menu_framerate": "Menu framerate",
            "same_as_ingame": "Same as in-game"
        },
        "problems": {
            "1": {
                "title": "Stutter while driving",
                "cause": "Chunks arrive faster than their pictures bake, and the car is drawn at its physics steps.",
                "why": "At 120 km/h about 50 new chunks a second reach the screen. Stock bakes each chunk's picture in the frame it arrives, and it draws the car and the camera at the last 100 Hz physics step, so the car rubber-bands against the street. These spread the bakes over frames, draw the car between its physics steps and keep trees in the bake. Rosewood town drive at the 240 cap: stock 153 fps (p99 36 ms), with these 235 fps (p99 8 ms)."
            },
            "2": {
                "title": "Low fps in a big horde",
                "cause": "Stock runs the whole zombie simulation on the game thread.",
                "why": "Every zombie's animation, decisions and drawing preparation run one after the other on the game thread, while the other cores idle. These run them on every core and skip checks that cannot change anything. The Louisville horde (about 2,000 zombies), same build with these off and on: 46 to 58 fps."
            },
            "3": {
                "title": "Long boot and loading",
                "cause": "Boot work runs one file at a time, and the loading screen waits for everything.",
                "why": "Stock parses scripts, animations and textures on one thread at boot and shows a loading screen until the whole cell is ready. These do the boot work on several threads with caches, and enter the world from the centre outwards with the last view on screen meanwhile. Launch to menu 7.4 to 5.0 s, Continue to the world 6.5 to 4.0 s."
            },
            "4": {
                "title": "Storms, fog and rain are slow",
                "cause": "Stock redraws fog rows and every wet square each frame.",
                "why": "Heavy fog is drawn as about 190 screen-wide rows per level, and rain re-packs every particle and puddle every frame. These draw fog in one pass, rain as repeated tiles and keep the puddles on the GPU. 120 km/h drive in heavy fog: 220 to 389 fps; thunderstorm: 83 to 131 fps."
            },
            "5": {
                "title": "Input feels laggy",
                "cause": "Input is read early and finished frames queue up for the GPU.",
                "why": "Stock reads the keyboard and mouse well before the frame they move is shown, and lets the driver queue frames. These read the newest input when a frame starts, keep the queue short and draw the cursor at the newest mouse position."
            },
            "6": {
                "title": "Screen tears or judders",
                "cause": "Borderless never gets variable refresh, and frames reach the screen unevenly.",
                "why": "A borderless window does not count as fullscreen for the desktop, so G-SYNC / FreeSync stay off, and frames reach the screen as soon as they are ready. These make the window count as fullscreen, keep the frame rate inside the display's range and hand frames over at even steps (judder 3.1 to 0.95 ms)."
            },
            "7": {
                "title": "Menus and inventory are slow",
                "cause": "Every window redraws every frame, with or without a change.",
                "why": "An open inventory took the Lua UI from 2 to 12 % of the game thread in stock. These redraw only what changed, the moment you act, and keep the map's labels while the view stays."
            },
            "8": {
                "title": "Laptop, Steam Deck or battery",
                "cause": "The game's threads land on slow cores and the GPU clock goes up and down.",
                "why": "On hybrid CPUs the game thread can end up on an efficient core; small GPUs spend frames at full resolution. These place the threads, hold the GPU clock steady, and render the world smaller when the GPU is the limit. The Low-end presets on the home page set them for you (4-core laptop, 120 km/h drive: 44 to 68 fps)."
            },
            "9": {
                "title": "I play with other mods",
                "cause": "A mod that patches the same game code can clash with an optimization.",
                "why": "PZ Optimization scans the Java mods of each launch and can switch off what they patch. Max performance keeps everything on and reports clashes; Max compatibility switches the affected settings off. The main menu's compatibility check lists what it found."
            }
        }
    }

    DIALOGS_EN = {
        "update": {
            "title": "PZ Optimization update",
            "tag": "Version",
            "changes": "Changes:",
            "up_to_date": "You are on the latest version!",
            "btn_update": "Update now",
            "btn_downloading": "Downloading...",
            "btn_installing": "Installing...",
            "btn_installed": "Installed, restart to finish",
            "btn_failed": "Update failed",
            "item_restart": "RESTART TO FINISH THE UPDATE",
            "item_update": "PZ OPTIMIZATION UPDATE"
        },
        "compat": {
            "title": "Mod compatibility check",
            "scanning": "Scanning active mods...",
            "safe": "No known mod conflicts found.",
            "conflicts_found": "Potential mod conflicts detected:",
            "item_compat": "PZ OPTIMIZATION MOD COMPATIBILITY CHECK",
            "profile_perf": "Max performance",
            "profile_compat": "Max compatibility",
            "profile_perf_tip": "Java mods are checked and listed here but switch nothing off; windows a mod draws in are reused like the game's own.",
            "profile_compat_tip": "The settings a Java mod patches are switched off so the mod meets the game code its author tested; windows a mod draws in are redrawn at the game's own rate.",
            "profile_status_running": "Running now: {profile}. Applies after a restart."
        },
        "overlay": {
            "item_turn_on": "SHOW PERFORMANCE OVERLAY",
            "item_turn_off": "HIDE PERFORMANCE OVERLAY",
            "keybinding": "Toggle Performance Overlay"
        }
    }

    en_data["ui"] = UI_EN
    en_data["dialogs"] = DIALOGS_EN
    en_data["options"] = en_options

    # 5. Write out json files
    with open(zh_path, "w", encoding="utf-8") as f:
        json.dump(zh_data, f, indent=2, ensure_ascii=False)
    print(f"Updated {zh_path} with {len(zh_options)} options")

    with open(en_path, "w", encoding="utf-8") as f:
        json.dump(en_data, f, indent=2, ensure_ascii=False)
    print(f"Updated {en_path} with {len(en_options)} options")

    # 6. Run i18n-build.py to generate Lua data
    ret = subprocess.run([sys.executable, str(ROOT / "scripts/i18n-build.py")], check=True)
    print(f"i18n-build exited with code {ret.returncode}")


if __name__ == "__main__":
    main()
