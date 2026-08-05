# Cloud GPU Workstation Lab

**Otwarte i praktyczne poradniki budowy wynajmowanych stacji GPU do tworzenia gier, AI, grafiki 3D, CAD, renderingu, symulacji i obliczeń naukowych.**

[English version](README.md)

> Wynajmuj mocny sprzęt tylko wtedy, gdy naprawdę pracujesz. Po zakończeniu zadania zatrzymuj maszynę. Kod, kopie zapasowe, bezpieczeństwo i koszty zachowuj pod kontrolą.

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

| Zadanie | Właściwy typ infrastruktury | Przykład |
|---|---|---|
| Edytor gry, praca interaktywna, grafika 3D | Wirtualna stacja robocza GPU | Windows + NVIDIA L4 |
| Trening modelu, self-play, symulacje wsadowe | Linux i węzeł lub klaster GPU | 1–8× H100 |
| Dokumentacja, Git i zarządzanie projektem | Tania maszyna CPU lub urządzenie lokalne | GitHub + przeglądarka |

Klaster 8× H100 nie przyspieszy zwykłego klikania w edytorze osiem razy. Jego przewaga pojawia się przy zadaniach, które można podzielić między wiele GPU.

## Zawartość

- [`docs/01-architecture.md`](docs/01-architecture.md) — wybór architektury
- [`docs/02-google-cloud-l4-windows.md`](docs/02-google-cloud-l4-windows.md) — stacja Windows + NVIDIA L4
- [`docs/03-runpod-h100-training.md`](docs/03-runpod-h100-training.md) — H100 do treningów
- [`docs/04-cost-control.md`](docs/04-cost-control.md) — zatrzymywanie, dyski, budżety i opłacalność
- [`docs/05-security.md`](docs/05-security.md) — RDP, zapora, sekrety i kopie
- [`docs/06-industry-use-cases.md`](docs/06-industry-use-cases.md) — zastosowania branżowe
- [`docs/07-affiliate-and-ethics.md`](docs/07-affiliate-and-ethics.md) — uczciwa afiliacja
- [`docs/08-troubleshooting.md`](docs/08-troubleshooting.md) — typowe problemy
- [`docs/09-case-study.md`](docs/09-case-study.md) — droga od 8× H100 do stacji L4
- [`tools/cost_estimator.py`](tools/cost_estimator.py) — kalkulator wynajem kontra zakup
- [`scripts/windows`](scripts/windows) — skrypty PowerShell
- [`scripts/linux`](scripts/linux) — kontrola GPU pod Linuksem

## Szybki start

```bash
python tools/cost_estimator.py   --purchase-cost 55000   --hourly-rate 10   --hours 100   --storage-monthly 150   --months 1
```

Na Windowsie uruchom PowerShell jako administrator:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
.\scripts\windows\install-dev-tools.ps1
.\scripts\windows\verify-workstation.ps1
```

Po pracy w Google Cloud:

**Compute Engine → Instancje maszyn wirtualnych → zaznacz maszynę → Zatrzymaj**

Poczekaj na stan **TERMINATED / Zatrzymana**. Praca GPU, CPU i RAM przestaje być naliczana, ale dyski trwałe oraz niektóre pozostałe zasoby mogą nadal kosztować.

## Najważniejsze zasady

1. Zamknięcie aplikacji RDP nie zatrzymuje maszyny.
2. Alert budżetowy zwykle nie jest twardą blokadą.
3. Zatrzymanie i usunięcie to różne operacje.
4. Dyski, migawki, statyczne IP i transfer mogą kosztować po zatrzymaniu.
5. Długie treningi zapisuj w checkpointach.
6. Porównuj całkowity koszt zadania.

## Afiliacja

Każdy link polecający musi być jasno oznaczony. Prowizja nie może wpływać na rekomendację techniczną ani prowadzić do ukrywania kosztów i ryzyka. Szczegóły: [`docs/07-affiliate-and-ethics.md`](docs/07-affiliate-and-ethics.md).

## Licencja

Apache License 2.0.
