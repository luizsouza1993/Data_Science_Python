{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Previsao_Teste.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOw70beFkX+NRQYz4Mrux2g",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/luizsouza1993/Projetos_Python/blob/main/Previsao_Simples.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "JqN3fyQax7vV"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from datetime import datetime, timedelta\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "datas = pd.DataFrame(pd.date_range((datetime.today() - timedelta(days = 1000)) , periods = 2000))"
      ],
      "metadata": {
        "id": "vq7XerOu2mBc"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "datas.rename(columns = {0: \"Data\"}, inplace=  True)"
      ],
      "metadata": {
        "id": "UFGiHjqS2uMa"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "datas[\"Data\"] = datas[\"Data\"].apply(lambda x: x.date())"
      ],
      "metadata": {
        "id": "9mrSg5Q_2v_E"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "datas[\"Dia_Semana\"] = datas[\"Data\"].apply(lambda x: x.strftime(\"%A\"))"
      ],
      "metadata": {
        "id": "ZZBH2jfb2yxP"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "feriados = pd.DataFrame({\"Data\": ['2022-01-01','2022-02-28','2022-03-01','2022-04-15','2022-04-21','2022-05-01','2022-06-16','2022-09-07','2022-10-12','2022-11-02','2022-11-15','2022-12-25'],\n",
        "                        \"Nome_Feriado\": ['Confraternização Universal','Carnaval','Carnaval','Paixão de Cristo','Tiradentes','Dia do Trabalho','Corpus Christi','Independência do Brasil','Nossa Sr.a Aparecida - Padroeira do Brasil','Finados','Proclamação da República','Natal']})"
      ],
      "metadata": {
        "id": "RkxbmW7V2z-R"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "feriados[\"Data\"] = feriados[\"Data\"].apply(lambda x : datetime.strptime(x,'%Y-%m-%d').date())"
      ],
      "metadata": {
        "id": "8c8HLG1N4R5j"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_previsao = pd.merge(datas, feriados, how = \"left\", right_on = \"Data\", left_on = \"Data\")"
      ],
      "metadata": {
        "id": "z2OHggRw223n"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_previsao.fillna(\"Não\", inplace = True)"
      ],
      "metadata": {
        "id": "nDTyTaQn24tt"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_previsao[\"Mes\"] = tabela_previsao[\"Data\"].apply(lambda x : x.strftime(\"%m\"))"
      ],
      "metadata": {
        "id": "VouwltZH2601"
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_previsao[\"Ano\"] = tabela_previsao[\"Data\"].apply(lambda x : x.strftime(\"%y\"))"
      ],
      "metadata": {
        "id": "tyXYpD3N29W4"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_previsao = tabela_previsao[tabela_previsao[\"Ano\"] ==\"22\"]"
      ],
      "metadata": {
        "id": "NQD9EZ7H2-x3"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def nomeia_data(dia, feriado):\n",
        "    if feriado == \"Não\" and dia == \"Saturday\":\n",
        "        return \"Sabado\"\n",
        "    elif feriado == \"Não\" and dia == \"Sunday\":\n",
        "        return \"Domingo\"\n",
        "    elif feriado != \"Não\":\n",
        "        return \"Feriado\"\n",
        "    else:\n",
        "        return \"Dia Util\""
      ],
      "metadata": {
        "id": "30xvIr713B0j"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "nomeia_data(\"Saturday\",\"Não\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "rjVcvTna3FgG",
        "outputId": "5f329702-e445-4bb6-8dea-82bd756cf11f"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Sabado'"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_previsao[\"Dia_Status\"] = tabela_previsao.apply(lambda x: nomeia_data(x.Dia_Semana, x.Nome_Feriado),axis=1)"
      ],
      "metadata": {
        "id": "y4T0LvUJ3GLw"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_resumo = tabela_previsao.groupby([\"Dia_Status\",\"Mes\"]).count().reset_index()"
      ],
      "metadata": {
        "id": "u49fx1rA3Hi7"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_resumo.rename(columns = {\"Data\":\"Quantidade\"}, inplace = True)\n",
        "tabela_resumo = tabela_resumo[[\"Dia_Status\",\"Mes\",\"Quantidade\"]]"
      ],
      "metadata": {
        "id": "k0hEEoQK3Ivl"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tabela_resumo"
      ],
      "metadata": {
        "id": "avEW6huU5lcs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*[texto em itálico](https://)*# Nova seção"
      ],
      "metadata": {
        "id": "RMjhW2EJ0Rpy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Nova seção"
      ],
      "metadata": {
        "id": "HWr4IsK10SJK"
      }
    }
  ]
}