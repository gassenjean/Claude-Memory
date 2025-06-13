#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Context Updater - Sistema de atualização automática do contexto Claude
Mantém a base de conhecimento sincronizada e organizada
"""

import os
import datetime
import json
from pathlib import Path
from typing import Dict, List, Optional

class ContextManager:
    def __init__(self, base_path: str = "./knowledge-base"):
        self.base_path = Path(base_path)
        self.sessions_path = self.base_path / "sessions"
        self.projects_path = self.base_path / "projects"
        self.insights_path = self.base_path / "insights"
        
        # Criar diretórios se não existirem
        for path in [self.sessions_path, self.projects_path, self.insights_path]:
            path.mkdir(parents=True, exist_ok=True)
    
    def create_session_log(self, project: str, context: str) -> str:
        """
        Cria log estruturado de sessão de trabalho
        """
        timestamp = datetime.datetime.now()
        session_id = timestamp.strftime("%Y%m%d_%H%M")
        
        session_data = {
            "session_id": session_id,
            "timestamp": timestamp.isoformat(),
            "project": project,
            "context": context,
            "decisions": [],
            "next_steps": [],
            "insights": [],
            "obstacles": [],
            "connections": []
        }
        
        filename = f"{session_id}_{project.lower().replace(' ', '_')}.json"
        filepath = self.sessions_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
        
        return str(filepath)
    
    def update_project_status(self, project_name: str, updates: Dict) -> bool:
        """
        Atualiza status de projeto específico
        """
        project_file = self.projects_path / f"{project_name.lower().replace(' ', '_')}.md"
        
        if not project_file.exists():
            print(f"Projeto {project_name} não encontrado. Criando novo arquivo...")
            self._create_project_template(project_file, project_name)
        
        # Aqui implementaríamos a lógica de update do markdown
        # Por enquanto, apenas logging
        print(f"Projeto {project_name} atualizado com: {updates}")
        return True
    
    def add_insight(self, category: str, insight: str, tags: List[str] = None) -> str:
        """
        Adiciona insight à base de conhecimento
        """
        timestamp = datetime.datetime.now()
        insight_id = timestamp.strftime("%Y%m%d_%H%M")
        
        insight_data = {
            "id": insight_id,
            "timestamp": timestamp.isoformat(),
            "category": category,
            "content": insight,
            "tags": tags or [],
            "source": "manual_entry"
        }
        
        # Organizar por categoria
        category_path = self.insights_path / category.lower().replace(' ', '_')
        category_path.mkdir(exist_ok=True)
        
        filename = f"{insight_id}_insight.json"
        filepath = category_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(insight_data, f, ensure_ascii=False, indent=2)
        
        return str(filepath)
    
    def generate_weekly_summary(self) -> Dict:
        """
        Gera resumo semanal de atividades e insights
        """
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=7)
        
        summary = {
            "period": {
                "start": start_date.isoformat(),
                "end": end_date.isoformat()
            },
            "sessions_count": 0,
            "projects_active": [],
            "key_insights": [],
            "next_week_focus": []
        }
        
        # Buscar sessões da semana
        for session_file in self.sessions_path.glob("*.json"):
            try:
                with open(session_file, 'r', encoding='utf-8') as f:
                    session = json.load(f)
                    session_date = datetime.datetime.fromisoformat(session['timestamp']).date()
                    
                    if start_date <= session_date <= end_date:
                        summary["sessions_count"] += 1
                        if session['project'] not in summary["projects_active"]:
                            summary["projects_active"].append(session['project'])
            except Exception as e:
                print(f"Erro ao processar {session_file}: {e}")
        
        return summary
    
    def _create_project_template(self, filepath: Path, project_name: str):
        """
        Cria template básico para novo projeto
        """
        template = f"""# 📊 {project_name}

## 📋 Status: [Definir Status]
**Última atualização**: {datetime.date.today().strftime("%d/%m/%Y")}  
**Próxima revisão**: [Definir data]  

## 🎯 Objetivo
[Descrição do objetivo principal]

## 📈 Status Atual
[Situação atual do projeto]

## 🚀 Próximos Passos
- [ ] [Ação 1]
- [ ] [Ação 2]
- [ ] [Ação 3]

## 💡 Insights Recentes
[Principais aprendizados e descobertas]

## ⚠️ Obstáculos
[Bloqueios e desafios identificados]

---
*Atualizado automaticamente pelo Context Manager*
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(template)
    
    def search_context(self, query: str, context_type: str = "all") -> List[Dict]:
        """
        Busca contextual na base de conhecimento
        """
        results = []
        search_paths = []
        
        if context_type in ["all", "sessions"]:
            search_paths.append(self.sessions_path)
        if context_type in ["all", "insights"]:
            search_paths.append(self.insights_path)
        
        for search_path in search_paths:
            for file_path in search_path.rglob("*.json"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Busca simples no conteúdo JSON
                        content_str = json.dumps(data, ensure_ascii=False).lower()
                        if query.lower() in content_str:
                            results.append({
                                "file": str(file_path),
                                "type": "session" if "sessions" in str(file_path) else "insight",
                                "data": data
                            })
                except Exception as e:
                    print(f"Erro ao buscar em {file_path}: {e}")
        
        return results

def main():
    """
    Exemplo de uso do Context Manager
    """
    manager = ContextManager()
    
    # Criar uma sessão de exemplo
    session_file = manager.create_session_log(
        project="Névoa AI Assistant",
        context="Desenvolvimento do MVP - Definição de arquitetura"
    )
    print(f"✅ Sessão criada: {session_file}")
    
    # Adicionar um insight
    insight_file = manager.add_insight(
        category="AI Development",
        insight="Claude tem funcionalidade de knowledge graph que pode ser útil para memória contextual",
        tags=["claude", "knowledge-graph", "memory", "ai"]
    )
    print(f"💡 Insight adicionado: {insight_file}")
    
    # Gerar resumo semanal
    summary = manager.generate_weekly_summary()
    print(f"\n📊 RESUMO SEMANAL:")
    print(f"Sessões: {summary['sessions_count']}")
    print(f"Projetos ativos: {', '.join(summary['projects_active'])}")
    
    # Buscar contexto
    results = manager.search_context("névoa")
    print(f"\n🔍 Resultados para 'névoa': {len(results)} itens encontrados")

if __name__ == "__main__":
    main()