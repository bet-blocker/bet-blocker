# BetBlocker

<p align="center">
  <img src="https://github.com/user-attachments/assets/7efbc8f9-8fe4-429e-8bae-1c6efa3a4453" alt="screen-home" width="1200">
</p>

[![Star on GitHub](https://img.shields.io/github/stars/jhowbhz/bet-blocker.svg?style=social)](https://github.com/jhowbhz/bet-blocker/stargazers)
<a href="https://github.com/jhowbhz/apigratis-sdk-php/network" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/jhowbhz/bet-blocker"></a>
<a href="https://github.com/jhowbhz/bet-blocker/issues" target="_blank"><img alt="GitHub issues" src="https://img.shields.io/github/issues/jhowbhz/bet-blocker"></a>
[![GitHub tag](https://img.shields.io/github/tag/jhowbhz/bet-blocker)](https://github.com/jhowbhz/bet-blocker/releases/?include_prereleases&sort=semver "View GitHub releases")
[![Minimum Python Version](https://img.shields.io/badge/python-%3E%3D%203.0-8892BF.svg?style=flat-square)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license "Go to license section")

A ideia deste repositório é criar um software focado em bloquear e impedir o acesso a sites de apostas. Essa ferramenta foi criada para ajudar pessoas que desejam se proteger contra os efeitos nocivos do vício em apostas online, oferecendo uma camada de proteção que limita o acesso a plataformas de jogos de azar.

## Objetivo
O BetBlocker foi pensado para que o próprio usuário ou familiares preocupados possam instalá-lo em dispositivos (computadores e, em breve, celulares) para bloquear sites de apostas de forma eficiente. Esse software visa ser um recurso acessível e de apoio para aqueles que reconhecem os riscos do vício em apostas e desejam tomar medidas preventivas.

## Requisitos básicos
- Python 2.7
- Windows ou Linux

## Instalação e utilização

Clone o repositório para sua máquina:
```bash
git clone https://github.com/jhowbhz/bet-blocker.git bet-blocker
```

Instale as dependencias:
```bash
cd bet-blocker && pip install -r requirements.txt
```

Para rodar o projeto:
```bash
python main.py
```

## Funcionamento
O BetBlocker realiza bloqueios por meio de configurações de firewall e ajustes no arquivo hosts para impedir o acesso a sites de apostas conhecidos. Além disso, oferece uma funcionalidade para configurar uma rede de apoio, uma opção que garante suporte ao usuário caso ele queira desbloquear ou remover o software de proteção em um momento de crise.

- Bloqueio de IP: Restrições realizadas via firewall para impedir a conexão com sites de apostas.
Configuração de DNS: Ajustes no arquivo hosts para impedir o acesso aos sites bloqueados.
- Rede de Apoio: Permite que familiares ou amigos sejam incluídos para suporte adicional.
Estado do Projeto
Atualmente, essa solução está em fase de Prova de Conceito (POC) e foi desenvolvida em Python. Contribuições são bem-vindas para que possamos avançar e melhorar o BetBlocker.

## Contribua
Acredita que pode ajudar a evoluir essa ideia? Caso sim, sinta-se à vontade para fazer uma pull request seguindo os passos a seguir:

 Crie um fork do repositório:
 <br>
![fork](https://github.com/user-attachments/assets/40a18cf5-031e-4134-bd73-e87cf22b57aa)

Clone o seu fork:
```
  git clone link_do_seu_repositório
```
Navegue até o diretório do projeto e instale as dependências:
```
  cd bet-blocker && pip install -r requirements.txt
```

Crie uma nova branch:
```
  git checkout -b feature/nome-da-sua-feature
```

Commite suas alterações:
```
  git add nome-do-arquivo
```

```
  git commit -m "descrição"
```

Puxe as alterações para o seu repositório:
```
  git push origin feature/nome-da-sua-feature
```

Abra uma nova Pull Request:
<br>
![pr](https://github.com/user-attachments/assets/0fb5947b-2a31-4240-b00d-12c9de24eee7)

Adicione um título e descrição para sua Pull Request:
<br>
![submmit](https://github.com/user-attachments/assets/a30c6f0a-8752-43c4-965a-279220b01279)

Feito, agora é só esperar para que sua Pull Request seja aceita, ou se caso seja encontrado algum erro de compatibilidade com o estado atual do projeto, ou qualquer outro problema, será adicionado um comentário e sua Pull Request será fechada. Sinta-se à vontade para abrir outra novamente e contribuir para o projeto.
