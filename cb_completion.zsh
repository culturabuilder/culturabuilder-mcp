#compdef cb
# ZSH completion for CulturaBuilder

_cb() {
    local -a commands
    commands=(
        'build:Construir componentes do projeto'
        'analyze:Analisar código e arquitetura'
        'deploy:Deploy com rollback automático'
        'improve:Melhorar qualidade do código'
        'metrics:Visualizar métricas de uso'
        'test:Executar testes com cobertura'
        'document:Gerar documentação bilíngue'
        'workflow:Gerenciar workflows complexos'
        'ai:Assistente IA para otimizações'
        'learn:Sistema de aprendizado interativo'
        'git:Gerenciamento Git bilíngue'
        'scaffold:Criar estrutura de projetos'
        'refactor:Refatorar código'
        'security:Auditoria de segurança'
        'performance:Otimização de performance'
        'config:Configurações do CulturaBuilder'
        'help:Mostrar ajuda'
    )

    local -a build_args
    build_args=(
        'frontend:Construir frontend'
        'backend:Construir backend'
        'all:Construir tudo'
        '--optimize:Otimizar build'
        '--clean:Limpar antes de construir'
        '--watch:Modo watch'
    )

    local -a analyze_args
    analyze_args=(
        '--deep:Análise profunda'
        '--focus:Focar em área específica'
        '--report:Gerar relatório'
        'security:Foco em segurança'
        'performance:Foco em performance'
        'quality:Foco em qualidade'
    )

    local -a test_args
    test_args=(
        'unit:Testes unitários'
        'integration:Testes de integração'
        'e2e:Testes end-to-end'
        'all:Todos os testes'
        '--coverage:Com cobertura'
        '--watch:Modo watch'
    )

    if (( CURRENT == 2 )); then
        _describe 'command' commands
    elif (( CURRENT == 3 )); then
        case "${words[2]}" in
            build)
                _describe 'build arguments' build_args
                ;;
            analyze)
                _describe 'analyze arguments' analyze_args
                ;;
            test)
                _describe 'test arguments' test_args
                ;;
            deploy)
                local -a deploy_args
                deploy_args=(
                    '--env:Ambiente de deploy'
                    'staging:Deploy para staging'
                    'production:Deploy para produção'
                    '--dry-run:Simulação'
                )
                _describe 'deploy arguments' deploy_args
                ;;
            *)
                _files
                ;;
        esac
    fi
}

compdef _cb cb