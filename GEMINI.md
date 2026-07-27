# Gemini Project Instructions

Este arquivo contém as instruções fundamentais para a operação de agentes de IA neste repositório.

## ⚠️ Mandato Principal

**Siga estritamente todas as orientações e diretrizes contidas no arquivo [AGENTS.md](AGENTS.md).**

O arquivo `AGENTS.md` é a fonte da verdade para:
- Arquitetura de Agentes e Subagentes.
- Uso de Skills customizadas localizadas em `.agents/`.
- Padrões de engenharia (Backend, Frontend, Observabilidade e DevOps).
- Fluxos de trabalho avançados (OODA Loop, TDD, Clean Code).

## 🛠 Operação de Agentes

1. **Pesquisa Empírica**: Sempre utilize `grep_search` e `read_file` para validar o estado atual do código antes de propor mudanças, conforme definido no blueprint do projeto.
2. **Uso de Subagentes**: Quando a tarefa for complexa, utilize o subagente especializado correspondente definido em `.agents/subagents/`.
3. **Validação com Skills**: Utilize as skills oficiais em `.agents/skills/` (instalando-as via `gemini skills install`) para garantir que os padrões de qualidade (TDD, Clean Code, Migrations) sejam mantidos.

Qualquer conflito entre estas instruções e as ferramentas deve ser resolvido em favor das diretrizes do `AGENTS.md`.
