# Git Notes

## Check where I am

```powershell
git branch
git branch --show-current
git status
```

## Switch to an existing branch

```powershell
git switch feature/neue-funktion
```

## Switch back to `main`

```powershell
git switch main
```

## Create a new branch and switch to it

```powershell
git switch -c feature/neues-feature
```

## Save changes

```powershell
git add .
git commit -m "Short description"
```

## Push a new branch for the first time

```powershell
git push -u origin feature/neue-funktion
```

## Push later changes on the same branch

```powershell
git push
```

## Pull latest changes from GitHub

```powershell
git pull
```

## Merge a finished feature into `main`

```powershell
git switch main
git pull
git merge feature/neue-funktion
git push
```

## Delete a branch after merging

```powershell
git branch -d feature/neue-funktion
git push origin --delete feature/neue-funktion
```

## Simple workflow

1. Check current branch:

```powershell
git branch --show-current
```

2. Switch to your feature branch if needed:

```powershell
git switch feature/neue-funktion
```

3. Work on the code
4. Save changes:

```powershell
git add .
git commit -m "What I changed"
```

5. Push changes:

```powershell
git push
```

## Quick rule

- `main` = stable version
- `feature/...` = new work
- new branch = once `git push -u origin ...`
- after that = `git push`

```
echo GIT_NOTES.md >> .gitignore
git rm --cached GIT_NOTES.md
git add .gitignore
git commit -m "Ignore local notes"
```
