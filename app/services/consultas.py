from fastapi import FastAPI, HTTPException
import requests


async def personajes_servicios():
    url = "https://spapi.dev/api/characters"
    personajes = []
    try:
        response = requests.get(url)
        data = response.json()
        if "data" in data:
            for character in data["data"]:
                if "name" in character:
                    familiares = await pregunta_persona(character["relatives"])
                    personajes.append(
                        {
                            'nombre': character["name"],
                            'genero': character["sex"],
                            'familiares': familiares
                        }
                    )
        else:
            return "Sin personajes"
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener los personajes: {str(e)}",
        )
    return personajes

async def pregunta_persona (relatives):
    personas = []
    for familiar in relatives:
        quest_nombre = requests.get(familiar["url"])
        reponse = quest_nombre.json()
        nombre_familiar = reponse["data"]["name"]
        relacion = familiar["relation"]
        personas.append(
            {
                'nombre': nombre_familiar,
                'parentesco': relacion
            }
        )
    return personas
