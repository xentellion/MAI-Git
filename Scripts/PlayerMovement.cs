using System;
using System.Collections;
using System.Collections.Generic;
using System.Security.Claims;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{

    public float acceleration = 40, speedLimit = 100, damping = 1.025f;
    private Vector3 velocity;
    private bool isGrounded;
    
    public void Move(Vector3 direction) {
        if (velocity.magnitude < speedLimit)
            velocity += direction * (acceleration * Time.deltaTime) / damping;
        else
            velocity = velocity.normalized * speedLimit;
    }

    private void FixedUpdate() {
        velocity /= damping;
        transform.position += velocity * Time.deltaTime;

        if (GroundCheck()) {
            velocity.y = 0;
        } else {
            velocity += Vector3.down * (9.81f * 2 * Time.deltaTime);
        }
    }

    bool GroundCheck() {

        RaycastHit hit;

        if (Physics.Raycast(transform.position, Vector3.down, out hit, 0.5f)) {
            return true;
        }
        
        return false;
    }
}
