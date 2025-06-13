#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Processador de Questionário - Criatividade e Paralisia por Análise
Transforma respostas do questionário em entidades e relações estruturadas para o knowledge graph
"""

import json
import datetime
from typing import Dict, List, Any

class QuestionnaireProcessor:
    def __init__(self):
        self.entity_base = {
            "name": "",
            "entityType": "",
            "observations": []
        }
        
        self.relation_base = {
            "from": "",
            "to": "",
            "relationType": ""
        }
        
        # Mapping de padrões para tipos de entidade
        self.pattern_mappings = {
            "perfectionist": "behavioral_pattern",
            "overthinking": "cognitive_pattern", 
            "creative_burst": "productivity_pattern",
            "decision_paralysis": "cognitive_block",
            "flow_state": "optimal_state"
        }
    
    def process_questionnaire(self, responses: Dict) -> Dict[str, Any]:
        """
        Processa respostas do questionário e gera estrutura para knowledge graph
        """
        entities = []
        relations = []
        insights = []
        
        # Criar entidade principal da pessoa
        person_entity = self._create_person_entity(responses)
        entities.append(person_entity)
        
        # Processar padrões cognitivos
        cognitive_patterns = self._extract_cognitive_patterns(responses)
        entities.extend(cognitive_patterns["entities"])
        relations.extend(cognitive_patterns["relations"])
        
        # Processar ritmos e energia
        energy_patterns = self._extract_energy_patterns(responses)
        entities.extend(energy_patterns["entities"])
        relations.extend(energy_patterns["relations"])
        
        # Processar objetivos e bloqueios
        goals_blocks = self._extract_goals_and_blocks(responses)
        entities.extend(goals_blocks["entities"])
        relations.extend(goals_blocks["relations"])
        
        # Gerar insights personalizados
        insights = self._generate_insights(responses)
        
        return {
            "entities": entities,
            "relations": relations,
            "insights": insights,
            "processing_date": datetime.datetime.now().isoformat(),
            "profile_summary": self._create_profile_summary(responses)
        }
    
    def _create_person_entity(self, responses: Dict) -> Dict:
        """
        Cria entidade principal da pessoa baseada nas respostas básicas
        """
        basic_info = responses.get("basic_info", {})
        self_definition = responses.get("self_definition", {})
        
        observations = [
            f"Idade: {basic_info.get('age', 'Não informado')}",
            f"Localização: {basic_info.get('location', 'Não informado')}",
            f"Profissão: {basic_info.get('profession', 'Não informado')}",
            f"Autodefinição: {self_definition.get('three_words', 'Não informado')}",
            f"Maior talento: {self_definition.get('biggest_talent', 'Não informado')}",
            f"Maior dificuldade: {self_definition.get('biggest_difficulty', 'Não informado')}",
            f"Motivação principal: {self_definition.get('motivation', 'Não informado')}",
            "Perfil: Criativo com paralisia por análise",
            "Status: Mapeamento ativo no knowledge graph"
        ]
        
        return {
            "name": basic_info.get("full_name", "User").replace(" ", "_"),
            "entityType": "person",
            "observations": observations
        }
    
    def _extract_cognitive_patterns(self, responses: Dict) -> Dict:
        """
        Extrai padrões cognitivos das respostas sobre pensamento e criatividade
        """
        entities = []
        relations = []
        
        thinking_patterns = responses.get("thinking_patterns", {})
        creative_process = responses.get("creative_process", {})
        analysis_paralysis = responses.get("analysis_paralysis", {})
        
        # Criar entidade para padrões de pensamento
        thinking_entity = {
            "name": "Thinking_Patterns",
            "entityType": "cognitive_system",
            "observations": [
                f"Ideias por dia: {creative_process.get('ideas_per_day', 'Não informado')}",
                f"Melhor momento para ideias: {creative_process.get('best_idea_time', 'Não informado')}",
                f"Tempo máximo analisando: {analysis_paralysis.get('max_analysis_time', 'Não informado')}",
                f"Principal bloqueio: {analysis_paralysis.get('main_block', 'Não informado')}",
                "Padrão: Excesso de análise antes da ação"
            ]
        }
        entities.append(thinking_entity)
        
        # Criar entidade para paralisia por análise
        paralysis_entity = {
            "name": "Analysis_Paralysis",
            "entityType": "cognitive_block",
            "observations": [
                f"Situação recente: {analysis_paralysis.get('recent_situation', 'Não informado')}",
                f"Como sai da paralisia: {analysis_paralysis.get('how_to_escape', 'Não informado')}",
                "Impacto: Bloqueia execução de ideias criativas"
            ]
        }
        entities.append(paralysis_entity)
        
        # Relações
        person_name = responses.get("basic_info", {}).get("full_name", "User").replace(" ", "_")
        relations.extend([
            {"from": person_name, "to": "Thinking_Patterns", "relationType": "exhibits"},
            {"from": person_name, "to": "Analysis_Paralysis", "relationType": "struggles_with"},
            {"from": "Analysis_Paralysis", "to": "Thinking_Patterns", "relationType": "disrupts"}
        ])
        
        return {"entities": entities, "relations": relations}
    
    def _extract_energy_patterns(self, responses: Dict) -> Dict:
        """
        Extrai padrões de energia e produtividade
        """
        entities = []
        relations = []
        
        energy_info = responses.get("energy_productivity", {})
        flow_states = responses.get("flow_states", {})
        
        # Criar entidade para ritmos naturais
        energy_entity = {
            "name": "Energy_Rhythms",
            "entityType": "biological_pattern",
            "observations": [
                f"Acordar natural: {energy_info.get('natural_wake', 'Não informado')}",
                f"Pico de energia: {energy_info.get('peak_energy', 'Não informado')}",
                f"Menor energia: {energy_info.get('low_energy', 'Não informado')}",
                f"Foco intenso (duração): {energy_info.get('intense_focus_duration', 'Não informado')}",
                f"Mudanças por hora: {energy_info.get('task_switches_per_hour', 'Não informado')}"
            ]
        }
        entities.append(energy_entity)
        
        # Criar entidade para estados de flow
        flow_entity = {
            "name": "Flow_States",
            "entityType": "optimal_state",
            "observations": [
                f"Condições para flow: {flow_states.get('flow_conditions', 'Não informado')}",
                f"Duração típica: {flow_states.get('flow_duration', 'Não informado')}",
                f"Interruptores de flow: {flow_states.get('flow_breakers', 'Não informado')}",
                f"Preferência de projetos: {flow_states.get('project_preference', 'Não informado')}"
            ]
        }
        entities.append(flow_entity)
        
        # Relações
        person_name = responses.get("basic_info", {}).get("full_name", "User").replace(" ", "_")
        relations.extend([
            {"from": person_name, "to": "Energy_Rhythms", "relationType": "follows"},
            {"from": person_name, "to": "Flow_States", "relationType": "achieves"},
            {"from": "Energy_Rhythms", "to": "Flow_States", "relationType": "enables"}
        ])
        
        return {"entities": entities, "relations": relations}
    
    def _extract_goals_and_blocks(self, responses: Dict) -> Dict:
        """
        Extrai objetivos e bloqueios específicos
        """
        entities = []
        relations = []
        
        goals = responses.get("goals_aspirations", {})
        
        # Criar entidades para objetivos principais
        for i, goal in enumerate(goals.get("top_3_projects", []), 1):
            if goal.strip():
                goal_entity = {
                    "name": f"Goal_{i}",
                    "entityType": "objective",
                    "observations": [
                        f"Descrição: {goal}",
                        f"Bloqueio: {goals.get('blocking_factors', 'Não informado')}",
                        "Status: Planejamento/Paralisia",
                        f"Timeline: 6 meses"
                    ]
                }
                entities.append(goal_entity)
                
                # Relação com pessoa
                person_name = responses.get("basic_info", {}).get("full_name", "User").replace(" ", "_")
                relations.append({
                    "from": person_name, 
                    "to": f"Goal_{i}", 
                    "relationType": "aspires_to"
                })
        
        return {"entities": entities, "relations": relations}
    
    def _generate_insights(self, responses: Dict) -> List[str]:
        """
        Gera insights personalizados baseados no padrão de respostas
        """
        insights = []
        
        # Análise de padrões de paralisia
        analysis_time = responses.get("analysis_paralysis", {}).get("max_analysis_time", "")
        if "meses" in analysis_time.lower():
            insights.append("Padrão de paralisia prolongada identificado - necessário intervenção em ciclos de análise")
        
        # Análise de energia vs criatividade
        peak_energy = responses.get("energy_productivity", {}).get("peak_energy", "")
        idea_time = responses.get("creative_process", {}).get("best_idea_time", "")
        if peak_energy and idea_time and peak_energy != idea_time:
            insights.append("Desalinhamento entre pico de energia e momento criativo - oportunidade de otimização")
        
        # Análise de execução
        creative_output = responses.get("creative_process", {}).get("what_happens_to_ideas", "")
        if "esquece" in creative_output.lower() or "não executa" in creative_output.lower():
            insights.append("Gap crítico entre geração de ideias e execução - necessário sistema de captura e priorização")
        
        return insights
    
    def _create_profile_summary(self, responses: Dict) -> str:
        """
        Cria resumo executivo do perfil
        """
        name = responses.get("basic_info", {}).get("full_name", "Usuário")
        main_difficulty = responses.get("self_definition", {}).get("biggest_difficulty", "paralisia por análise")
        main_talent = responses.get("self_definition", {}).get("biggest_talent", "criatividade")
        
        return f"""
        Perfil de {name}:
        - Talento principal: {main_talent}
        - Desafio principal: {main_difficulty}
        - Padrão: Alta criatividade com dificuldade de execução
        - Necessidade: Sistema de suporte para transformar ideias em ação
        - Abordagem recomendada: Intervenções anti-paralisia + estruturação de execução
        """

def main():
    """
    Exemplo de uso do processador
    """
    # Exemplo de respostas (seria preenchido pelo usuário)
    sample_responses = {
        "basic_info": {
            "full_name": "João Silva",
            "age": "32",
            "location": "São Paulo, SP",
            "profession": "Designer"
        },
        "self_definition": {
            "three_words": "Criativo, analítico, perfeccionista",
            "biggest_talent": "Gerar ideias inovadoras",
            "biggest_difficulty": "Decidir qual ideia executar",
            "motivation": "Criar soluções que impactem positivamente as pessoas"
        },
        "analysis_paralysis": {
            "recent_situation": "Ficou 2 semanas analisando qual framework usar para um projeto",
            "max_analysis_time": "1 mês para decidir mudança de carreira",
            "main_block": "Medo de escolher a opção não-otima",
            "how_to_escape": "Conversar com alguém de confiança"
        }
    }
    
    processor = QuestionnaireProcessor()
    result = processor.process_questionnaire(sample_responses)
    
    print("📊 PROCESSAMENTO CONCLUÍDO")
    print(f"Entidades criadas: {len(result['entities'])}")
    print(f"Relações mapeadas: {len(result['relations'])}")
    print(f"Insights gerados: {len(result['insights'])}")
    print("\n" + result['profile_summary'])

if __name__ == "__main__":
    main()