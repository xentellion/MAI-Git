using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(PlayerMovement))]
public class Controller : MonoBehaviour
{
    private PlayerMovement movement;
    private Vector3 inputDirection;

    private void Awake() {
        movement = GetComponent<PlayerMovement>();
    }

    private void Update() {

        inputDirection = new Vector3(Input.GetAxisRaw("Horizontal"), 0, Input.GetAxisRaw("Vertical")).normalized;
        if (inputDirection.magnitude != 0)
            movement.Move(inputDirection);
        
    }
}
