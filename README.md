# 🔐 INIYA PDF Cracker

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green)
![Status](https://img.shields.io/badge/status-Stable-success)

> Brute force un fichier PDF protégé par mot de passe.  
> 💻 Made with 💙 by **Iniya Merci**

---

## 🧠 Description

`INIYA PDF Cracker` est un outil en Python permettant de déverrouiller un fichier PDF protégé en utilisant une attaque brute force basée sur une wordlist personnalisée.  
Il est rapide, simple, portable et entièrement personnalisable.

---

## ⚙️ Fonctionnalités

✅ Brute force sur fichiers PDF  
✅ Interface en ligne de commande (CLI) stylée  
✅ Installation automatique des dépendances  
✅ Signature ASCII personnalisée `INIYA`  
✅ Génération de fichier déverrouillé automatiquement  
✅ Compatible avec Termux, Linux, Windows, macOS

---

## 🚀 Installation & Utilisation

### 📦 Cloner le projet

```bash
git clone https://github.com/Perians/pdf-cracker.git
cd pdf-cracker
### 🔑 Wordlist personnalisée

Le succès du craquage dépend fortement de la qualité de votre wordlist.

#### ✅ 1. Télécharger une wordlist puissante (exemples) :
- [rockyou.txt (classique)](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
- [SecLists – Passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)

#### ✅ 2. Générer une wordlist personnalisée :
Vous pouvez créer une wordlist simple avec `crunch` :

```bash
pkg install crunch
crunch 4 6 abc123 -o my_wordlist.txt
---

## ⚠️ Avertissement

> **Cet outil est fourni uniquement à des fins éducatives et de tests de sécurité légitimes.**
>
> Son but est d'aider :
> - les chercheurs en cybersécurité,
> - les pentesters,
> - et les étudiants à mieux comprendre la sécurité des fichiers PDF.

L'auteur **décline toute responsabilité** en cas de mauvaise utilisation.  
N'utilisez jamais cet outil sans l'autorisation explicite du propriétaire du fichier ciblé.

---
