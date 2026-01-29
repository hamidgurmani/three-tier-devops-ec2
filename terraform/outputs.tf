output "public_ip" {
  value = aws_instance.jenkins.public_ip
}

output "ssh_command" {
  value = "ssh -i ${var.key_name}.pem ubuntu@${aws_instance.jenkins.public_ip}"
}

