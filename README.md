# Spaceapps-2019-Luasa
Solução desenvolvida durante o SpaceApps SP

## Solução

Nós pensamos em uma solução que nos permitisse educar as futuras gerações para que as mesmas conheçam mais sobre as missões da NASA, pois a NASA é um orgão publico que depende da opinião publica para que os impostos sejam convertidos para as agencias. Mas hoje, 20% dos americanos não acreditam que o homem foi a lua e isso pode ser um problema para o projeto de 2028, onde a NASA quer retornar a Lua.

Por isso a ideia foi de usar realidade aumentada para educar as futuras gerações através de uma ficha que as crianças receberiam nas escolas e através de um web app que pode ser utilizado em qualquer celular, seria possível as crianças e educadores interagirem com a lua.

## Tecnologia utilizada

A aplicação foi desenvolvida se utilizando python e usando o framework Flask-Restful para o backend, onde a aplicação ao final foi containerizada usando o docker, já a parte da realidade aumentada, foi utilizado o código do <a href="https://github.com/jeromeetienne/ar.js">jeromeetienne<a> para se gerar a lua, usando a sua biblioteca AR.js;

## Equipe Luasa
<a href="https://www.linkedin.com/in/milenaabade/">Milena Abade<a>,
  <a href="https://www.linkedin.com/in/pedrocherubini/">Pedro Cherubini<a>,
    <a href="https://www.linkedin.com/in/brenoyano/">Breno Yano<a>
<img src="https://media.licdn.com/dms/image/C5622AQGfDmHoUQQZoA/feedshare-shrink_1280/0?e=1575504000&v=beta&t=4sh1WQV7kPHp2svkQ3uUFRzIniZipDhWVNsol1kbDhk" height="400" width="600">

## Utilização:

#### Para utiliza-lo, clone o repositório;
#### Tenha o Docker e o docker-compose instalado;
#### Na pasta do repositório, rode o comando em um terminal:
####   docker-compose up -d
#### Com a aplicação rodando entre em localhost:5000
#### Para testar o AR clique em Teste a Luasa.
