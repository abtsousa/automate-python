#! python3

import re, pyperclip

# Regex for phone numbers
phoneRegex = re.compile(r'[29]\d{8}')

# Regex for postal codes
postalRegex = re.compile(r"(\d{4}-\d{3}) ([a-zA-Z ]+)\s")

# Get text from clipboard
text = '''
12 Estrada Nacional 3 2350-471 Torres Novas 913967424
100 Avarias, Lda. Estrada Nacional 8 - Lavradio 2500-315 Caldas da Rainha 262001361
100 Peças – Comércio de Peças e Acessórios Auto, Lda. Rua das Barreiras, nº147 4590-140 Paços de Ferreira
100% Auto, Lda. Estrada de Sto. Eloy, n.º 12 2650-458 Amadora 964050691 http://100auto.pt/pt/
105N Motor, Lda. Estrada Nacional 105 Nº 737, Lordelo 4815-135 Guimarães 253722790 http://nmotor.pt/
111 Sport – Comércio de Automóveis, Lda. Rua Alcorredores, n.º 82 - Ponte de Vilela 3020-925 Coimbra 239913036 www.111sport.pt
1234 Car Unipessoal, Lda. Rua Espregueira Mendes, n.º 1 - 5º Esq. 2720-076 Amadora 963761394 http://www.1234car.pt/
125 Glassauto, Unipessoal, Lda. Rua Dr. Afonso Costa, nº 18 8700-359 Olhão
24 Horas - Comércio de Automóveis, Unipessoal Lda. Estrada Nacional 107, 85 4425-138 Maia 916158060
2M1J - Soluções Auto, Lda. Rua Boqueirão Ferro, Armazém 1 2680-177 Camarate 215908200 www.npecas.com.pt
324 Auto, Lda. Avenida da Conduta, 324 4510-523 Fânzeres
355 Automóveis, Unipessoal, Lda. Rua Padre Domingos Joaquim Pereira, n.º 1293 4760-563 Vila Nova de Famalicão 919191395
3P Auto, Lda. Rua das Águas, 588 3700-028 São João da Madeira
3S Auto, Lda. Av. Eng. José Afonso Moreira Figueiredo, n.º 85 4470-285 Maia 223163938
4 Motion – Automóveis Lda. Estrada D. Miguel (Alto do Tronco), S/N Jovim – Gondomar
4 Road Unipessoal, Lda. Rua Agostinho Marques, n.º 30 - 4º Esq. 4700-409 Braga 253042998
41 Peças e Acessórios, Lda. Estrada Nacional 9, 5 - Loja 2 - Soito 2560-124 Ponte do Rol TVD 261931456
A Construtora de Radiadores de Vítor Fernandes & José Fernandes,
Lda. Calçada do Carrascal, 169 A 1900-132 Lisboa 218480122 www.construtoraderadiadores.com
A Construtora de Radiadores de Vítor Fernandes & José Fernandes,
Lda. (Odivelas) Rua Manuel Pereira Borges - Ponte da Bica - Ramada 2650-501 Odivelas 219800290 /
219810607
A Moderna Oureense – Reparadora de Automóveis, Lda. Avenida D. Nuno Álvares Pereira 2490-483 Ourém 249540690
A Moto Power Car - Comércio de Viaturas, Lda. Estrada Nacional 249 - Abóboda 2785-035 Cascais 214444456
A&R Aguiar - Reparações Automóveis, Lda. (Filial) Zona Industrial do Monte da Barca, Lote 8 2100-051 Coruche 243679512
A&R Aguiar - Reparações Automóveis, Lda. (Sede) Rua Felicidade Páscoa, 71 2100-519 Fajarda 243679512
A. Alberto Praça Jerónimo Lda. Via Sul (R. Almeida Pessanha) 5340 Macedo de Cavaleiros
A. B. P. - Auto Boutique de Peças, Unipessoal Lda. Rua do Sistelo, 346 4435-452 Gondomar 224882360
A. Barata Manutenção Automóvel, Unipessoal Lda. Rua Dr. José Fernandes, 24 2745-292 Queluz 214300616
A. Braz Heleno, Lda. E. N., 109 - Ponte da Pedra 2400-240 Regueira de Pontes
A. C. - Manutenção e Comércio de Veículos, S. A. Rua da ETAR, 4 - Apartado 76 - Zona Industrial 3770-068 Oiã 262915190
A. C. - Manutenção e Comércio de Veículos, S. A. (Guarda) Parque Industrial, Lote 16 6300-625 Guarda 262915190
A. C. - Manutenção e Comércio de Veículos, S. A. (Mangualde) Quinta do Bacelo, Cruzamento de São Cosmado - Apartado 176 3530-258 Mangualde 262915190
A. C. - Manutenção e Comércio de Veículos, S. A. (Turquel) Estrada Nacional 1, Km 88 - Charneca do Carvalhal 2460-796 Turquel 262915190
A. Coelho, S. A. Estrada Nacional 1, km 88 - Charneca do Carvalhal - Turquel 2460-796 Alcobaça 262915140
A. F. Anacleto - Reparação Automóveis, Lda. Rua 25 de Abril, Lote 112 Moinhos da Funcheira 2700-000 Amadora 214918483
A. F. Anacleto - Reparação Automóveis, Lda. (Sede) Rua 5 de Outubro, 33 A 2650-333 Moinhos da Funcheira 214945313
A. F. J. C. Unipessoal Lda. Rua de São Julião, 2136 4990-670 Ponte de Lima 258741084
A. Ladeira, Lda. Vale do Grou 3750-870 Águeda 234624167
A. M. Amaral - Peças e Acessórios Auto, Lda. Avenida dos Bons Amigos, 51 A 2735-145 Cacém 219140299
A. M. Esteves Martins, Lda. Avenida dos Bombeiros Voluntários, 387 4585-359 Rebordosa 224112648
A. M. Gouveia, Sociedade Unipessoal, Lda. Avenida dos Combatentes da Grande Guerra, 60 B 2900-328 Setúbal 265547800 /1/2
A. M. Oliveira, Lda. Rua D. Manuel Ferreira da Silva, 10 - Arrotinha 3860-210 Estarreja 234842500
A. Moretti, Unipessoal Lda. Rua Tomás Gonzaga, 13 - 1º Esq. 4050-607 Porto
A. Neves Reboques de Fátima, Lda. Rua Central, n.º 261 - Loureira 2495-122 Santa Catarina da Serra 249533374
A. Nogueira Vieira Unipessoal, Lda. Av. do Brasil, 72-B 2700-134 Amadora 211945701
A. Rodrigues & Filhos, Lda. Cruzamento do Pontão, R/C 3240-490 Ansião 236620110
A. S. Ferreira, Unipessoal Lda. Rua Serpa Pinto 8550-467 Monchique 282912263
A.24 Euroreboques, Lda. Cerro do Outro 8200-468 Paderne 289571000
A.A. Costa Gouveia, Lda. Zona Industrial de Oliveira do Hospital 3400-060 Oliveira do Hospital 238603054
'''


# Extract postal code and phone from text
extPhone = phoneRegex.findall(text)
extPostal = postalRegex.findall(text)

print(extPhone)
print(extPostal)