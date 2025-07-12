#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TH_e_ART_h_MAN - Complete Application Launcher
Main launcher for the complete 902 artists integration
Version: 2.0 - Production Ready
Date: 12.07.2025

This is the COMPLETE version with:
- 902 artists from SupaGruen integration
- Professional web interface
- AI chat integration
- Expanded artist gallery
- Full production features
"""

import sys
import os
import subprocess
import time
import webbrowser
import json
from pathlib import Path

def check_python_env():
    """Check Python environment and virtual env"""
    print("🐍 Sprawdzanie środowiska Python...")
    
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Środowisko wirtualne znalezione")
        if sys.platform == "win32":
            python_exe = venv_path / "Scripts" / "python.exe"
        else:
            python_exe = venv_path / "bin" / "python"
        
        if python_exe.exists():
            print("✅ Python w venv gotowy")
            return str(python_exe)
    
    print("⚠️  Używam systemowego Pythona")
    return sys.executable

def check_dependencies():
    """Check if all dependencies are installed"""
    print("📦 Sprawdzanie zależności...")
    try:
        import flask
        import requests
        print("✅ Wszystkie zależności dostępne")
        return True
    except ImportError as e:
        print(f"❌ Brakuje zależności: {e}")
        return False

def start_api_server(python_exe):
    """Start the Flask API server"""
    print("🚀 Uruchamianie serwera API...")
    
    # Start the API server
    api_script = Path("copilot_workspace") / "api_server.py"
    if not api_script.exists():
        print("❌ Nie znaleziono api_server.py")
        return None
    
    try:
        process = subprocess.Popen(
            [python_exe, str(api_script)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0
        )
        print("✅ Serwer API uruchomiony")
        print(f"   PID: {process.pid}")
        print(f"   URL: http://localhost:4040")
        return process
    except Exception as e:
        print(f"❌ Błąd uruchamiania serwera: {e}")
        return None

def wait_for_server(url="http://localhost:4040", timeout=30):
    """Wait for server to be ready"""
    print("⏳ Czekam na gotowość serwera...")
    
    import requests
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print("✅ Serwer gotowy!")
                return True
        except:
            pass
        time.sleep(1)
    
    print("⚠️  Serwer może nie być w pełni gotowy")
    return False

def open_browser():
    """Open browser with the application"""
    print("🌐 Otwieranie przeglądarki...")
    try:
        webbrowser.open("http://localhost:4040")
        print("✅ Otwarto: http://localhost:4040")
    except Exception as e:
        print(f"⚠️  Nie udało się otworzyć przeglądarki: {e}")

def show_success_info():
    """Show success information"""
    print("\n🎯 DOSTĘPNE STRONY:")
    print("   🏠 Główny interfejs: http://localhost:4040")
    print("   🎨 Explorer artystów: http://localhost:4040/artists.html")
    print("   📡 API status: http://localhost:4040/api/status")
    
    print("\n" + "="*80)
    print("                            GOTOWE!                             ")
    print("="*80)
    print("      902 artystow dostepnych                                  ")
    print("      29 ruchow artystycznych                                  ")
    print("      AI chat aktywny                                          ")
    print("      Wyszukiwarka gotowa                                      ")
    print("="*80)
    print("      http://localhost:4040                                    ")
    print("                                                              ")
    print("      Nacisnij Ctrl+C aby zatrzymac serwer                       ")
    print("="*80)

def main():
    """Main launcher function"""
    print("\n" + "="*80)
    print("                        TH_e_ART_h_MAN                      ")
    print("                Artists Integration Project                      ")
    print("                       LAUNCHER v2.0                            ")
    print("="*80)
    print("    ")
    print("    902 artystow gotowych do uzycia!")
    print("    Uruchamianie serwera...")
    print("    ")
    
    # Check requirements
    print("Sprawdzanie wymagan...")
    if not Path("copilot_workspace").exists():
        print("❌ Brak katalogu copilot_workspace")
        return False
    
    if not Path("data").exists():
        print("❌ Brak katalogu data")
        return False
    
    print("Wszystkie pliki obecne")
    
    # Check Python environment
    python_exe = check_python_env()
    if not python_exe:
        return False
    
    # Check dependencies
    if not check_dependencies():
        print("Zainstaluj zależności: pip install -r requirements.txt")
        return False
    
    # Start API server
    server_process = start_api_server(python_exe)
    if not server_process:
        return False
    
    # Wait for server
    wait_for_server()
    
    # Open browser
    open_browser()
    
    # Show success info
    show_success_info()
    
    try:
        # Keep the launcher running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Zamykanie aplikacji...")
        if server_process:
            server_process.terminate()
        return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("❌ Uruchomienie nie powiodło się")
        input("Naciśnij Enter aby zakończyć...")
        sys.exit(1)
    else:
        print("✅ Aplikacja zakończona pomyślnie")
        sys.exit(0)