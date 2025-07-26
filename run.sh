#!/bin/bash
uvicorn ai_chat.main:app --reload &
uvicorn comms_system.main:app --reload &
uvicorn hospital_data.main:app --reload &
