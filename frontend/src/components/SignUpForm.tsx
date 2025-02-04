import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { useState } from "react";
import axios from "axios";

export default function SignUpForm() {
  const [formData, setFormData] = useState({
    fullname: "",
    username: "",
    email: "",
    password: "",
  });

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(formData);
    try {
      const response = await axios.post(
        `${import.meta.env.VITE_BACKEND_URL}/auth/sign-up`,
        {
          full_name: formData.fullname,
          username: formData.username,
          email: formData.email,
          password: formData.password,
        }
      );
      console.log(response.data);
    } catch (e) {
      console.log("error", e);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <div className="w-full min-h-screen flex items-center justify-center bg-gray-900 text-slate-200 p-4">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle className="text-2xl font-bold text-center">
            Fill the Details
          </CardTitle>
        </CardHeader>
        <CardContent>
          <form className="space-y-4" onSubmit={handleSubmit}>
            <div className="space-y-2">
              <Label htmlFor="fullName">Full Name</Label>
              <Input
                className="rounded-xl"
                id="fullName"
                name="fullname"
                value={formData.fullname}
                onChange={handleChange}
                placeholder="John Doe"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="username">Username</Label>
              <Input
                className="rounded-xl"
                value={formData.username}
                name="username"
                onChange={handleChange}
                id="username"
                placeholder="johndoe"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input
                className="rounded-xl"
                value={formData.email}
                onChange={handleChange}
                id="email"
                name="email"
                type="email"
                placeholder="john@example.com"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input
                className="rounded-xl"
                value={formData.password}
                onChange={handleChange}
                name="password"
                id="password"
                type="password"
              />
            </div>
            <Button
              className="w-full bg-white rounded-xl text-gray-900 hover:bg-white hover:text-gray-900"
              type="submit"
            >
              Sign Up
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
