import json
from urllib import parse, request
from urllib.error import HTTPError, URLError

from django.shortcuts import render


REST_COUNTRIES_BASE = "https://restcountries.com/v3.1"


def _fetch_json(url):
    try:
        with request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode("utf-8")), None
    except HTTPError as exc:
        return None, f"API error: {exc.code}"
    except URLError:
        return None, "Could not connect to Rest Countries API."
    except (json.JSONDecodeError, TimeoutError):
        return None, "Invalid response from API."


def _build_country_details(country):
    currencies_data = country.get("currencies") or {}
    currencies = []
    for code, item in currencies_data.items():
        currencies.append(
            {
                "code": code,
                "name": item.get("name", "N/A"),
                "symbol": item.get("symbol", "N/A"),
            }
        )

    languages = list((country.get("languages") or {}).values())
    latlng = country.get("latlng") or []

    return {
        "name": country.get("name", {}).get("common", "N/A"),
        "capital": ", ".join(country.get("capital") or []) or "N/A",
        "region": country.get("region", "N/A"),
        "subregion": country.get("subregion", "N/A"),
        "borders": ", ".join(country.get("borders") or []) or "N/A",
        "area": country.get("area", "N/A"),
        "google_maps": country.get("maps", {}).get("googleMaps"),
        "population": country.get("population", "N/A"),
        "timezones": ", ".join(country.get("timezones") or []) or "N/A",
        "continents": ", ".join(country.get("continents") or []) or "N/A",
        "currencies": currencies,
        "languages": ", ".join(languages) if languages else "N/A",
        "latitude": latlng[0] if len(latlng) > 0 else "N/A",
        "longitude": latlng[1] if len(latlng) > 1 else "N/A",
        "flag_image": (country.get("flags") or {}).get("png") or (country.get("flags") or {}).get("svg"),
        "coat_of_arms": (country.get("coatOfArms") or {}).get("png") or (country.get("coatOfArms") or {}).get("svg"),
        "start_of_week": country.get("startOfWeek", "N/A"),
        "postal_code_format": (country.get("postalCode") or {}).get("format", "N/A"),
        "independent": bool(country.get("independent", False)),
    }


def country_search(request):
    query = request.GET.get("q", "").strip()
    countries = []
    error = None

    if query:
        encoded_query = parse.quote(query)
        url = f"{REST_COUNTRIES_BASE}/name/{encoded_query}?fields=name,cca3,capital,region,flags"
        data, error = _fetch_json(url)
        if data:
            countries = sorted(data, key=lambda item: item.get("name", {}).get("common", ""))

    return render(request, "app/home.html", {"query": query, "countries": countries, "error": error})


def country_detail(request, code):
    url = f"{REST_COUNTRIES_BASE}/alpha/{parse.quote(code)}"
    data, error = _fetch_json(url)
    country_details = None

    if data and isinstance(data, list):
        country_details = _build_country_details(data[0]) if data else None

    return render(
        request,
        "app/detail.html",
        {
            "country": country_details,
            "error": error or ("Country not found." if not country_details else None),
        },
    )


# Backward-compatible names if old urls still reference these.
index = country_search
search_country = country_search