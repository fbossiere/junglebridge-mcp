# Développement

Ouvrir ce dépôt dans VS Code, puis **Dev Containers: Reopen in Container**.
Docker doit être démarré. Le premier démarrage télécharge les images et outils.
Le conteneur installe les dépendances verrouillées et les hooks Git.
L'environnement Python du conteneur est distinct du `.venv` de l'hôte.

Dans le terminal du conteneur, lancer `claude` et se connecter à son compte.
Claude Code est installé à version fixe ; son état est conservé dans un volume
Docker propre à ce devcontainer. Aucun compte n'est connecté automatiquement.
Les permissions habituelles restent actives. Les règles `.claude` sont des
aides de travail, pas une frontière de sécurité contre toutes les commandes shell.
Le conteneur ne monte ni le trousseau, ni les clés SSH, ni le socket Docker de l'hôte.
Le réseau sortant n'est pas filtré ; ne pas utiliser de vrais dossiers candidats.

Sans conteneur : installer uv, puis `make bootstrap`.

```sh
make check       # Ruff, mypy, Bandit, pytest et couverture
make audit       # vulnérabilités des dépendances runtime verrouillées (réseau)
make build       # wheel et distribution source
make format      # formatage automatique
```

`uv.lock` fait partie du dépôt. Mettre à jour les dépendances avec `uv lock --upgrade`,
contrôler le diff et relancer les vérifications. FastMCP et les outils directs
étant fixés dans pyproject.toml, modifier aussi leur version pour les mettre à jour.
Les images de base suivent des tags ; pour une reproductibilité binaire stricte,
fixer leurs digests lors de la préparation de release.

Références : [FastMCP](https://gofastmcp.com/getting-started/installation),
[Claude Code en devcontainer](https://code.claude.com/docs/en/devcontainer),
[configuration Claude Code](https://code.claude.com/docs/en/settings).
