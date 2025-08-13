# CulturaBuilder MCP - Script de Instalação para Windows
# PowerShell script para instalação automática

# Verificar se está rodando como administrador
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{
    Write-Host "Este script precisa ser executado como Administrador." -ForegroundColor Red
    Write-Host "Clique com botão direito no PowerShell e escolha 'Executar como Administrador'" -ForegroundColor Yellow
    Exit 1
}

# Banner
Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║          CulturaBuilder MCP - Instalador             ║" -ForegroundColor Cyan
Write-Host "║        Framework para Claude Code - v3.0.0           ║" -ForegroundColor Cyan
Write-Host "╚═══════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
function Check-Python {
    Write-Host "Verificando Python..." -ForegroundColor Blue
    
    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) {
        $version = python --version 2>&1
        Write-Host "✓ Python encontrado: $version" -ForegroundColor Green
        
        # Verificar versão
        if ($version -match "Python (\d+)\.(\d+)") {
            $major = [int]$matches[1]
            $minor = [int]$matches[2]
            
            if ($major -ge 3 -and $minor -ge 8) {
                Write-Host "✓ Python versão compatível" -ForegroundColor Green
                return $true
            } else {
                Write-Host "✗ Python muito antigo. Versão 3.8+ necessária" -ForegroundColor Red
                return $false
            }
        }
    } else {
        Write-Host "✗ Python não encontrado" -ForegroundColor Red
        return $false
    }
}

# Instalar Python via winget
function Install-Python {
    Write-Host "`nInstalando Python..." -ForegroundColor Blue
    
    # Verificar se winget está disponível
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if ($winget) {
        Write-Host "Usando winget para instalar Python..." -ForegroundColor Yellow
        winget install Python.Python.3.12 --silent
        
        # Atualizar PATH
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
        
        Write-Host "✓ Python instalado" -ForegroundColor Green
        Write-Host "IMPORTANTE: Feche e reabra o PowerShell após a instalação!" -ForegroundColor Yellow
        return $true
    } else {
        # Baixar e instalar manualmente
        Write-Host "winget não encontrado. Baixando Python..." -ForegroundColor Yellow
        
        $url = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe"
        $output = "$env:TEMP\python-installer.exe"
        
        Invoke-WebRequest -Uri $url -OutFile $output
        
        Write-Host "Instalando Python (isso pode demorar)..." -ForegroundColor Yellow
        Start-Process -FilePath $output -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
        
        Remove-Item $output
        
        Write-Host "✓ Python instalado" -ForegroundColor Green
        return $true
    }
}

# Instalar CulturaBuilder
function Install-CulturaBuilder {
    Write-Host "`nInstalando CulturaBuilder MCP..." -ForegroundColor Blue
    
    try {
        python -m pip install --upgrade pip
        python -m pip install culturabuilder
        Write-Host "✓ CulturaBuilder instalado com sucesso" -ForegroundColor Green
        return $true
    } catch {
        Write-Host "Erro ao instalar CulturaBuilder" -ForegroundColor Red
        Write-Host $_.Exception.Message -ForegroundColor Red
        
        # Tentar instalação alternativa
        Write-Host "Tentando instalação alternativa..." -ForegroundColor Yellow
        
        # Clonar do GitHub
        $tempDir = "$env:TEMP\culturabuilder-mcp"
        git clone https://github.com/culturabuilder/culturabuilder-mcp.git $tempDir 2>$null
        
        if (Test-Path $tempDir) {
            Set-Location $tempDir
            python -m pip install .
            Set-Location -
            Remove-Item -Recurse -Force $tempDir
            Write-Host "✓ CulturaBuilder instalado do código fonte" -ForegroundColor Green
            return $true
        }
        
        return $false
    }
}

# Configurar CulturaBuilder
function Configure-CulturaBuilder {
    Write-Host "`nConfigurando CulturaBuilder no Claude..." -ForegroundColor Blue
    
    python -m culturabuilder install --quick
    
    Write-Host "✓ Configuração completa" -ForegroundColor Green
}

# Verificar instalação
function Verify-Installation {
    Write-Host "`nVerificando instalação..." -ForegroundColor Blue
    
    $claudeDir = "$env:USERPROFILE\.claude"
    
    if (Test-Path $claudeDir) {
        Write-Host "✓ Diretório .claude encontrado" -ForegroundColor Green
        
        if (Test-Path "$claudeDir\CLAUDE.md") {
            Write-Host "✓ Arquivos de configuração instalados" -ForegroundColor Green
            return $true
        }
    }
    
    Write-Host "✗ Instalação pode ter falhado" -ForegroundColor Red
    return $false
}

# Main
function Main {
    # Verificar ou instalar Python
    if (-not (Check-Python)) {
        if (-not (Install-Python)) {
            Write-Host "`nErro ao instalar Python. Por favor, instale manualmente:" -ForegroundColor Red
            Write-Host "https://python.org/downloads/" -ForegroundColor Yellow
            Exit 1
        }
    }
    
    # Instalar CulturaBuilder
    if (-not (Install-CulturaBuilder)) {
        Write-Host "`nErro ao instalar CulturaBuilder" -ForegroundColor Red
        Exit 1
    }
    
    # Configurar
    Configure-CulturaBuilder
    
    # Verificar
    if (Verify-Installation) {
        Write-Host ""
        Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Green
        Write-Host "✓ CulturaBuilder MCP instalado com sucesso!" -ForegroundColor Green
        Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Green
        Write-Host ""
        Write-Host "Próximos passos:" -ForegroundColor Yellow
        Write-Host "1. Abra o Claude Desktop ou Claude Code"
        Write-Host "2. Digite: /cb:help"
        Write-Host "3. Explore os comandos disponíveis!"
        Write-Host ""
        Write-Host "Documentação: https://github.com/culturabuilder/culturabuilder-mcp" -ForegroundColor Blue
        Write-Host "Suporte: https://github.com/culturabuilder/culturabuilder-mcp/issues" -ForegroundColor Blue
    }
}

# Executar
Main