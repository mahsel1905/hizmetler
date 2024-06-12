dil = input("Choose your language (tr/en): ")

if dil == "en":
    print("""
    services
    ------------------------
    1- watch news
    2- watch euro 2024 last match
    """)

    while True:
        secim = input("What would you like mom : ")
        if secim == "1":
            import webbrowser
            webbrowser.open("https://www.youtube.com/watch?v=F8LhXToVb0o&t")
        elif secim == "2":
            import webbrowser
            webbrowser.open("https://www.youtube.com/watch?v=W5w9Cw29JUs")
        else:
            print("Invalid choice. Please try again.")

elif dil == "tr":
    print("""
    hizmetler
    ------------------------
    1- haberleri izle
    2- türkiyenin son maçını izle
    """)

    while True:
        secim = input("Ne istersin annecim:")
        if secim == "1":
            import webbrowser
            webbrowser.open("https://www.youtube.com/watch?v=F8LhXToVb0o&t")
        elif secim == "2":
            import webbrowser
            webbrowser.open("https://www.youtube.com/watch?v=W5w9Cw29JUs")
        else:
            print("Geçersiz seçim. Lütfen tekrar dene.")

else:
    print("Invalid language choice. Please choose between 'tr' or 'en'.")

