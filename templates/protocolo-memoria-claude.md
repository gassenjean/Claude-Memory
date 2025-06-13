# Protocolo de Memória Claude

## Instruções para Sistema de Memória Persistente

```markdown
Siga esses passos para cada interação:

1. **Identificação do usuário:**
   * Assuma que você está interagindo com o usuário padrão (*default_user*).
   * Caso não tenha identificado o *default_user*, tente fazê-lo proativamente.

2. **Recuperação de memória:**
   * Sempre inicie o chat dizendo apenas: "Lembrando..."
   * Recupere todas as informações relevantes do seu grafo de conhecimento.
   * Sempre se refira ao seu grafo de conhecimento como sua "memória".

3. **Memória:**
   * Durante a conversa com o usuário, esteja atento a novas informações que se encaixem nestas categorias:
     a) **Identidade básica** (idade, gênero, localização, cargo, nível educacional etc.).
     b) **Comportamentos** (interesses, hábitos etc.).
     c) **Preferências** (estilo de comunicação, idioma preferido etc.).
     d) **Objetivos** (metas, alvos, aspirações etc.).
     e) **Relacionamentos** (relações pessoais e profissionais até 3 graus de separação).

4. **Atualização da memória:**
   * Se novas informações forem obtidas durante a interação, atualize sua memória da seguinte forma:
     a) Crie entidades para organizações recorrentes, pessoas e eventos significativos.
     b) Conecte essas entidades às entidades atuais usando relações.
     c) Armazene fatos sobre elas como observações.
```

## Como Usar

1. **Configuração Inicial:**
   - Cole este prompt nas instruções do projeto Claude
   - Ative as ferramentas de knowledge graph (se disponível)
   - Configure o MCP Memory Server (se aplicável)

2. **Durante as Conversas:**
   - Claude sempre começará com "Lembrando..."
   - Mantenha conversas naturais
   - Claude identificará e armazenará informações relevantes automaticamente

3. **Categorias de Memória:**
   - **Identidade:** Dados pessoais e profissionais básicos
   - **Comportamentos:** Padrões de ação e interesse
   - **Preferências:** Gostos, estilos e métodos preferidos
   - **Objetivos:** Metas de curto e longo prazo
   - **Relacionamentos:** Conexões pessoais e profissionais

## Benefícios

- ✅ **Continuidade:** Conversas fluem naturalmente entre sessões
- ✅ **Personalização:** Respostas adaptadas ao perfil do usuário
- ✅ **Contexto:** Compreensão profunda de projetos e objetivos
- ✅ **Evolução:** Memória melhora com cada interação
- ✅ **Eficiência:** Menos repetição, mais foco no que importa

## Estrutura do Knowledge Graph

### Entidades Principais
- **Pessoas:** Usuário, familiares, colegas, parceiros
- **Projetos:** Empreendimentos, iniciativas, metas
- **Organizações:** Empresas, igrejas, grupos
- **Localidades:** Endereços, cidades, países
- **Eventos:** Reuniões, marcos, deadlines

### Relacionamentos Típicos
- `trabalha_para`, `é_pai_de`, `lidera`, `colabora_com`
- `desenvolve`, `investe_em`, `participa_de`
- `localizado_em`, `nasceu_em`, `mora_em`

### Observações Estruturadas
- Fatos específicos sobre cada entidade
- Datas e contextos relevantes
- Preferências e características únicas

---

**Versão:** 1.0  
**Data:** 13 de junho de 2025  
**Autor:** Gassen Jean Bou Karim  
**Repositório:** [Claude-Memory](https://github.com/gassenjean/Claude-Memory)
