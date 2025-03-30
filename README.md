# ConstruFacil

Este aplicativo foi criado para a cadeira de Projeto Interdisciplinar para Sistemas de Informação I do 1º período do curso de Sistemas de informação pela Faculdade (UFRPE). O objetivo do App é facilitar  aos usuário que não são familiarizados com os conceitos utilizados na construção civil, onde os mesmos possam realizar seus próprios cálculos de quantidade de tijolos, cerâmica, capacidade de água em um reservatório e de rejunte.

## Funcionalidades

- Calculo da quantidade de tijolos, onde o resultado mostrado é em unidades para tijolos de 4, 6, 8 e 9 furos.
- Calculo da quantidade de cerâmica, onde o resultado mostrado é em m² para colocação padrão como também a colocação em diagonal.
- Calculo da capacidade de água em um reservatório, onde o resultado mostrado é em m³ e em litros.
- Calculo da quantidade de rejunte, onde o resultado mostrado é kg para rejunte do tipo epóxi, acrílico e cimentício.

## Pré-requisitos

Antes de executar o programa, certifique-se de que as seguintes bibliotecas estão instaladas em seu ambiente Python:

- `kivy`

Para instalar a biblioteca necessária, execute o seguinte comando no terminal:

**Atenção!**
**Os comando abaixo é para usuários Windows:**

```bash
python -m pip install --upgrade pip setuptools virtualenv
python -m venv kivy_venv
kivy_venv\Scripts\activate
python -m pip install "kivy[base]" kivy_examples
```

**Atenção!**
**Os comando abaixo é para usuários Linux:**

```bash
python3 -m pip install --upgrade pip setuptools virtualenv
python3 -m venv kivy_venv
source kivy_venv/bin/activate
python3 -m pip install "kivy[base]" kivy_examples
```

- `kivyMD`

Para instalar a biblioteca necessária, execute o seguinte comando no terminal:

**Atenção!**
**Os comando abaixo é para usuários Windows e Linux:**

```bash
pip install kivymd
```

## Contribuidores

- André dos Santos Barbosa

## Licença

MIT License

Copyright (c) 2025 Andre Barbosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Licença (Português do Brasil)

Licença MIT

Copyright (c) 2025 Andre Barbosa

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e arquivos de documentação associados (o "Software"), para lidar
no Software sem restrição, incluindo, sem limitação, os direitos
para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e / ou vender
cópias do Software, e para permitir que as pessoas a quem o Software é
fornecido para fazê-lo, sujeito às seguintes condições:

O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todos
cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO,
ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA E NÃO VIOLAÇÃO. EM NENHUMA HIPÓTESE O
AUTORES OU TITULARES DE DIREITOS AUTORAIS SÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTROS
RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, DELITO OU DE OUTRA FORMA, DECORRENTE DE,
FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO
PROGRAMAS.
