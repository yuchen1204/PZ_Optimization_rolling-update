-- pzopt: internationalization (i18n) helper for PZ Optimization.
-- Reads translation data from PzoptI18nData (generated from i18n/*.json by scripts/i18n-build.py)
-- and gracefully falls back to the original English text whenever a translation or entry is missing.

PzoptI18n = {}

local currentLang = nil

-- Detect current game language.
-- Returns "zh_cn" for Chinese (Simplified or Traditional), or "en_us" as fallback.
function PzoptI18n.detectLang()
    local ok, lang = pcall(function() return Translator.getLanguage() end)
    if not ok or not lang then return "en_us" end
    local name = tostring(lang:name() or ""):upper()
    if name == "CN" or name == "CH" or name == "TC" or string.find(name, "CHIN") then
        return "zh_cn"
    end
    return "en_us"
end

function PzoptI18n.getLang()
    if not currentLang then
        currentLang = PzoptI18n.detectLang()
    end
    return currentLang
end

-- Refresh language on boot / reload
function PzoptI18n.refresh()
    currentLang = PzoptI18n.detectLang()
end

-- Translate a dot-separated path, e.g. PzoptI18n.t("ui.buttons.export", "Export settings")
function PzoptI18n.t(path, fallback)
    local lang = PzoptI18n.getLang()
    if lang == "en_us" or not PzoptI18nData or not PzoptI18nData[lang] then
        return fallback
    end
    local cur = PzoptI18nData[lang]
    for seg in string.gmatch(path, "[^.]+") do
        if type(cur) == "table" then
            cur = cur[seg]
        else
            return fallback
        end
    end
    if type(cur) == "string" and cur ~= "" then
        return cur
    end
    return fallback
end

-- pzopt: true on a Chinese language (options file uses it for the hand-broken dialog text)
function PzoptI18n.isZh()
    return PzoptI18n.getLang() == "zh_cn"
end

-- Get option label or tip, e.g. PzoptI18n.getOption("treesInChunkTexture", "label", entry.label)
function PzoptI18n.getOption(key, field, fallback)
    local lang = PzoptI18n.getLang()
    if lang == "en_us" or not PzoptI18nData or not PzoptI18nData[lang] then
        return fallback
    end
    local opts = PzoptI18nData[lang].options
    if opts and opts[key] and opts[key][field] and opts[key][field] ~= "" then
        return opts[key][field]
    end
    return fallback
end

if Events and Events.OnLanguageChanged then
    Events.OnLanguageChanged.Add(function()
        PzoptI18n.refresh()
    end)
end
