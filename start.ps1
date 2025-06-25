# start.ps1

Write-Host " Iniciando o container..." -ForegroundColor Green

# Para e remove o container se já existir
docker rm -f gestor 2>$null

# Roda o container com a imagem existente
docker run -p 8000:8000 -v ${PWD}:/app -v ${PWD}\db:/app/db -v ${PWD}\staticfiles:/app/staticfiles gestor

