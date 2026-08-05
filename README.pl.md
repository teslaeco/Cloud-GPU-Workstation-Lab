# Cloud GPU Workstation Lab

[![CI](https://github.com/teslaeco/Cloud-GPU-Workstation-Lab/actions/workflows/ci.yml/badge.svg)](https://github.com/teslaeco/Cloud-GPU-Workstation-Lab/actions/workflows/ci.yml)
[![Licencja](https://img.shields.io/badge/licencja-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](pyproject.toml)
[![Dokumentacja](https://img.shields.io/badge/docs-English%20%7C%20Polski-informational.svg)](README.md)

**Otwarte poradniki i przetestowane narzędzia do budowy wynajmowanych stacji GPU dla twórców gier, AI, grafiki 3D, CAD, renderingu, symulacji i obliczeń naukowych.**

[English version](README.md) · [Indeks dokumentacji](docs/README.md) · [Współpraca](CONTRIBUTING.md) · [Bezpieczeństwo](SECURITY.md)

> Wynajmuj mocny sprzęt tylko wtedy, gdy naprawdę pracujesz. Po zakończeniu zadania zatrzymuj maszynę. Kod, kopie zapasowe, bezpieczeństwo i koszty zachowuj pod kontrolą.

## Status projektu

Repozytorium jest aktywnie rozwijanym projektem edukacyjnym. Usługi chmurowe, limity, sterowniki, ceny i regulaminy programów partnerskich zmieniają się. Przed utworzeniem płatnych zasobów sprawdzaj aktualną dokumentację dostawcy.

## Po co powstało to repozytorium

Niezależny twórca lub mały zespół nie zawsze musi kupować drogą stację roboczą albo serwer z ośmioma kartami GPU. Stację w chmurze można uruchomić na kilka godzin pracy w Unreal Engine, a osobny klaster GPU tylko na czas treningu AI, renderowania, symulacji lub przetwarzania dużych zbiorów danych.

Repozytorium powstało na podstawie praktycznego doświadczenia z:

- środowiskiem 8× NVIDIA H100 używanym podczas OpenAI Parameter Golf,
- stacją Google Cloud z Windowsem i kartą NVIDIA L4,
- pracą zdalną z telefonu z Androidem,
- Unreal Engine, narzędziami AI, grafiką 3D i zarządzaniem projektem przez Git.

Celem nie jest przekonywanie, że jeden dostawca jest najlepszy do wszystkiego. Celem jest nauczenie ludzi dobierania właściwej maszyny do zadania, przygotowania pracy przed uruchomieniem GPU i unikania opłat za bezczynny sprzęt.

## Dla kogo

- twórcy gier,
- inżynierowie AI,
- graficy 3D, animatorzy i zespoły VFX,
- architekci oraz użytkownicy CAD/BIM,
- naukowcy i zespoły obliczeniowe,
- projekty geoinformatyczne i satelitarne,
- twórcy wideo i render farmy,
- studenci i niezależni twórcy bez drogiego komputera.

## Strategia dwóch maszyn

| Zadanie | Zalecany typ infrastruktury | Przykład |
|---|---|---|
| Edytor gry, praca interaktywna, grafika 3D | Wirtualna stacja robocza GPU | Windows + NVIDIA L4 |
| Trening modelu, self-play, symulacje wsadowe | Linux i węzeł lub klaster GPU | 1–8× H100 |
| Dokumentacja, Git i zarządzanie projektem | Tania maszyna CPU lub urządzenie lokalne | GitHub + przeglądarka |

Klaster 8× H100 nie przyspieszy zwykłego klikania w edytorze osiem razy. Jego przewaga pojawia się przy zadaniach, które można podzielić między wiele GPU.

## Zacznij tutaj

1. Przeczytaj [opis architektury](docs/01-architecture.md).
2. Wybierz [stację Google Cloud z L4](docs/02-google-cloud-l4-windows.md) albo [środowisko treningowe H100](docs/03-runpod-h100-training.md).
3. Przed utworzeniem zasobów przeczytaj rozdziały o [kontroli kosztów](docs/04-cost-control.md) i [bezpieczeństwie](docs/05-security.md).
4. Po instalacji uruchom skrypty weryfikacyjne.
5. Po pracy zatrzymaj zasoby obliczeniowe i potwierdź ich końcowy status w panelu dostawcy.

## Struktura repozytorium

```text
.
├── .github/                 # CI, formularze zgłoszeń i szablon PR
├── docs/                    # Architektura, instalacja, koszty i bezpieczeństwo
├── scripts/
│   ├── linux/               # Kontrola GPU pod Linuksem
│   └── windows/             # Instalacja i weryfikacja Windows
├── tests/                   # Testy jednostkowe i integracyjne CLI
├── tools/                   # Niezależne od dostawcy narzędzia pomocnicze
├── README.md                # Strona główna po angielsku
└── README.pl.md             # Strona główna po polsku
```

Pełny indeks: [`docs/README.md`](docs/README.md).

## Szybki start

### Porównanie wynajmu z zakupem

```bash
python tools/cost_estimator.py \
  --purchase-cost 55000 \
  --hourly-rate 10 \
  --hours 100 \
  --storage-monthly 150 \
  --months 1 \
  --currency PLN
```

### Instalacja narzędzi na Windows

Uruchom PowerShell jako administrator po wcześniejszym przejrzeniu skryptu:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
.\scripts\windows\install-dev-tools.ps1
.\scripts\windows\verify-workstation.ps1
```

### Kontrola węzła GPU z Linuksem

```bash
bash scripts/linux/check-gpu.sh
```

### Testy lokalne

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
```

## Najważniejsze zasady kosztowe

1. Zamknięcie aplikacji RDP nie zatrzymuje maszyny.
2. Alert budżetowy zwykle nie jest twardą blokadą wydatków.
3. Zatrzymanie i usunięcie to różne operacje.
4. Dyski, migawki, statyczne adresy IP i transfer mogą kosztować po zatrzymaniu maszyny.
5. Długie treningi zapisuj w checkpointach.
6. Porównuj całkowity koszt zadania, a nie wyłącznie reklamowaną cenę GPU za godzinę.

## Afiliacja

Każdy link polecający musi być jasno oznaczony. Prowizja nie może wpływać na rekomendację techniczną ani prowadzić do ukrywania kosztów, ograniczeń i ryzyka. Szczegóły: [`docs/07-affiliate-and-ethics.md`](docs/07-affiliate-and-ethics.md).

Repozytorium nie zawiera obecnie nieoznaczonych linków afiliacyjnych.

## Współpraca

Przeczytaj [`CONTRIBUTING.md`](CONTRIBUTING.md). Każda większa zmiana powinna opisywać cel, ryzyko, kompatybilność, testy i wpływ na dokumentację. Zmiany rozwijamy w osobnych Pull Requestach i scalamy dopiero po zielonym CI.

## Cytowanie

Metadane do cytowania znajdują się w [`CITATION.cff`](CITATION.cff).

## Licencja

Apache License 2.0. Zobacz [`LICENSE`](LICENSE).
